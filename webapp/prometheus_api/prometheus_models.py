"""
Copyright 2023 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import List


class MetricType(Enum):
    gauge = 'gauge'


@dataclass
class BaseMetric:
    value: int

    def to_metric(self, identifier: str) -> str:
        data = asdict(self)
        label_list: list[str] = []
        for key, value in data.items():
            if key == 'value':
                continue
            value = value.replace('"', '')
            label_list.append(f'{key}="{value}"')
        return f'{identifier}{{{",".join(label_list)}}} {self.value}'


@dataclass
class SourceMetric(BaseMetric):
    source: str


@dataclass
class ParkingSiteMetric(BaseMetric):
    source: str
    parking_site_uid: str
    parking_site_name: str


@dataclass
class Metrics:
    help: str
    type: MetricType
    identifier: str
    metrics: List[BaseMetric] = field(default_factory=list)

    def to_metrics(self) -> List[str]:
        return [f'# HELP {self.identifier} {self.help}', f'# TYPE {self.identifier} {self.type.name}'] + [
            metric.to_metric(self.identifier) for metric in self.metrics
        ]
