"""
Copyright 2024 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from flask_openapi.decorator import Response, ResponseData
from flask_openapi.schema import ArrayField, IntegerField, JsonSchema, ObjectField, StringField

generic_parking_site_schema = JsonSchema(
    title='Generic Parking Site Push Response',
    properties={
        'summary': ObjectField(
            properties={
                'static_success_count': IntegerField(minimum=0),
                'realtime_success_count': IntegerField(minimum=0),
                'error_count': IntegerField(minimum=0),
            },
        ),
        'errors': ArrayField(
            items=ObjectField(
                properties={
                    'message': StringField(),
                    'parking_site_uid': StringField(nullable=True),
                    'source_uid': StringField(),
                },
            ),
        ),
    },
)

generic_parking_site_example = {
    'summary': {'static_success_count': 27, 'realtime_success_count': 27, 'error_count': 0},
    'errors': [],
}

generic_parking_site_response = Response(ResponseData(generic_parking_site_schema, generic_parking_site_example))
