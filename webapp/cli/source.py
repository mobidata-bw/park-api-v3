"""
Copyright 2023 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from pathlib import Path

import click
from flask.cli import AppGroup

from webapp.dependencies import dependencies
from webapp.services.import_service import ParkingSiteGenericImportService, ParkingSiteXlsxImportService

source_cli = AppGroup('source', help='Source related commands')


@source_cli.command('init-converters', help='init converters')
def cli_source_init_converters():
    parking_site_import_generic_service = ParkingSiteGenericImportService(
        parking_site_repository=dependencies.get_parking_site_repository(),
        source_repository=dependencies.get_source_repository(),
        **dependencies.get_base_service_dependencies(),
    )
    parking_site_import_generic_service.update_sources_static()
    parking_site_import_generic_service.update_sources_realtime()


@source_cli.command('xlsx-import', help='import parking sites from xlsx file')
@click.argument('source')
@click.argument('import_file_path', type=click.Path(dir_okay=False, path_type=Path))
def cli_import_parking_sites_xlsx(source: str, import_file_path: Path):
    parking_site_xlsx_import_service = ParkingSiteXlsxImportService(
        parking_site_repository=dependencies.get_parking_site_repository(),
        source_repository=dependencies.get_source_repository(),
        **dependencies.get_base_service_dependencies(),
    )
    parking_site_xlsx_import_service.load_and_import_parking_sites(source, import_file_path)


@source_cli.command('generic-import', help='import parking sites from generic source')
@click.argument('source')
def cli_import_parking_sites_generic(source: str):
    parking_site_import_generic_service = ParkingSiteGenericImportService(
        parking_site_repository=dependencies.get_parking_site_repository(),
        source_repository=dependencies.get_source_repository(),
        **dependencies.get_base_service_dependencies(),
    )
    parking_site_import_generic_service.update_source_static(source)
    parking_site_import_generic_service.update_source_realtime(source)
