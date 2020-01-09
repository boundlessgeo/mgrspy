# mgrspy Changelog

## 0.3.1

2020-01-09

### Added

- Projection transformation support for `pyproj` package (1.9.5+ required)
- **Note:** `pyproj` versions 2.0.x thru 2.1.x may cause errors (1.9.6 or 2.2.0+ recommended))
- Switched package dependency for projection transformations from `gdal` (used as `osgeo.osr`) to `pyproj`
- If found, `osgeo.osr` is _still preferred_ unless `MGRSPY_USE_PROJ` environment variable is set
- Bulk test of 1200+ populated places from Natural Earth project
- Debug logging to test suite

### Fixed

- Projection transformation errors due to PROJ v6+ axis ordering changes
- See: https://trac.osgeo.org/gdal/wiki/rfc73_proj6_wkt2_srsbarn#Axisorderissues

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
