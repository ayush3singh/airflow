#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import pytest

from airflow.providers.fab.www import app as application
from airflow.providers.fab.www.security import permissions

from tests_common.test_utils.config import conf_vars
from unit.fab.auth_manager.api_endpoints.api_connexion_utils import create_user, delete_user
from unit.fab.auth_manager.views import _assert_dataset_deprecation_warning
from unit.fab.utils import client_with_login


@pytest.fixture(scope="module")
def fab_app():
    with conf_vars(
        {
            (
                "core",
                "auth_manager",
            ): "airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager",
        }
    ):
        yield application.create_app(enable_plugins=False)


@pytest.fixture(scope="module")
def user_roles_reader(fab_app):
    yield create_user(
        fab_app,
        username="user_roles",
        role_name="role_roles",
        permissions=[
            (permissions.ACTION_CAN_READ, permissions.RESOURCE_ROLE),
            (permissions.ACTION_CAN_READ, permissions.RESOURCE_WEBSITE),
        ],
    )

    delete_user(fab_app, "user_roles")


@pytest.fixture
def client_roles_reader(fab_app, user_roles_reader):
    fab_app.config["WTF_CSRF_ENABLED"] = False
    return client_with_login(
        fab_app,
        username="user_roles_reader",
        password="user_roles_reader",
    )


@pytest.mark.db_test
class TestRolesListView:
    def test_role_model_view(self, client_roles_reader, recwarn):
        resp = client_roles_reader.get("/roles/list/", follow_redirects=True)

        _assert_dataset_deprecation_warning(recwarn)
        assert resp.status_code == 200
