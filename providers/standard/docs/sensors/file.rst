 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.



.. _howto/operator:FileSensor:

FileSensor
==========

Use the :class:`~airflow.providers.standard.sensors.filesystem.FileSensor` to detect files appearing in your local
filesystem. You need to have connection defined to use it (pass connection id via ``fs_conn_id``).
Default connection is ``fs_default``.

.. exampleinclude:: /../src/airflow/providers/standard/example_dags/example_sensors.py
    :language: python
    :dedent: 4
    :start-after: [START example_file_sensor]
    :end-before: [END example_file_sensor]

Also for this job you can use sensor in the deferrable mode:

.. exampleinclude:: /../src/airflow/providers/standard/example_dags/example_sensors.py
    :language: python
    :dedent: 4
    :start-after: [START example_file_sensor_async]
    :end-before: [END example_file_sensor_async]
