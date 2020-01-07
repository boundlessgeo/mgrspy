# mgrspy Changelog

## 0.3.1

2020-01-07

### Added

- Switched projection transformations (and dependency) from `gdal` to `pyproj` package
- Bulk test of 1200+ populated places from Natural Earth project
- Debug logging to test suite

### Fixed

- Projection errors with GDAL's OSR against PROJ v6+ for projection axis

## 0.3.0

2019-10-22

### Added

- `geotrans` 3.8 half-multiplier (optional, off by default)
- Copyright to Planet Federal
- Function to clean up user-input MGRS coordinates
- Added debug logging
- Treat UPS zones as 00 identifier

### Fixed

- Added missing scale computation for easting/northing multiplier
- Make source code PEP8-ish compliant
