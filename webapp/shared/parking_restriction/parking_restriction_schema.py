"""
Copyright 2025 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from flask_openapi.decorator import Schema
from flask_openapi.schema import (
    EnumField,
    IntegerField,
    JsonSchema,
    StringField,
)

from webapp.models.parking_restriction import ParkingAudience

parking_restriction_schema = JsonSchema(
    title='ParkingRestriction',
    properties={
        'parking_spot_id': IntegerField(
            minimum=1,
            required=False,
            description='ParkingSpot ID, generated by ParkAPI Service.',
        ),
        'parking_site_id': IntegerField(
            minimum=1,
            required=False,
            description='ParkingSite ID, generated by ParkAPI Service.',
        ),
        'type': EnumField(
            enum=ParkingAudience,
            required=False,
            description='If type is not set, all audiences are restricted.',
        ),
        'hours': StringField(required=False, maxLength=512, description='Opening times in OSM format'),
        'max_stay': StringField(
            required=False,
            maxLength=256,
            description='Maximum stay period, based on ISO 8601 duration format.',
        ),
    },
)

parking_restriction_example = {}

parking_restriction_component = Schema('ParkingRestriction', parking_restriction_schema, parking_restriction_example)
