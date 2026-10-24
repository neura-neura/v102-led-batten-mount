# Revision history and provenance

## Reference

Independent original clip design for one V-102 LED batten under a shelf. The lamp body is approximately 1150 × 23.5 × 14 mm and 120 g. The model marking and approximate label code did not establish a manufacturer drawing or a confirmed compatible downloadable clip. The supplied lamp photograph and owner measurements guided the design.

## R01

- Inner wall spacing: 24.1 mm.
- Tongue thickness: 0.6 mm.
- Nominal entry variants: 0.2, 0.3, 0.4 mm per side.
- The owner tested the 0.2 mm version and reported that it fitted but was loose.
- The 0.3 and 0.4 mm versions remain physically untested; they are archived for reference.

## R02 — current, owner-confirmed fit

- The owner requested a 1 mm smaller lateral dimension and 0.5 mm greater tongue engagement.
- Both arms moved inward 0.5 mm: inner spacing changed from 24.1 to 23.1 mm.
- Nominal entry relative to the lamp changed from 0.2 to 0.7 mm per side. The increase was applied once.
- Tongue projection from the wall remained 0.5 mm.
- Base, holes, tongue thickness, and vertical position remained unchanged.
- A native English FreeCAD project reproduces this geometry through a spreadsheet and native solid operations.
- The owner subsequently confirmed that the last delivered version worked. This repository records that as a successful **fit**, without adding unreported installation, material, load, or thermal-test claims.

## File provenance

`stl/v102-mount-r02-confirmed-fit.stl` is a byte-preserved copy of the FreeCAD-derived STL delivered immediately before the owner's success report. The English FreeCAD file is regenerated from the same nominal geometry with translated object labels, aliases, spreadsheet text, and notes. Its exported equivalent is `stl/v102-mount-r02-regenerated.stl`. Small mesh tessellation differences between exporters do not imply a dimensional revision.

The optional axial stop is a separate earlier experimental design. It was not part of the successful-fit confirmation. Earlier concepts based on the reversed groove geometry are intentionally excluded.

The measurement map is schematic. It labels the owner's measurement locations, not a certified drawing of the lamp profile. The dimensional mount drawing is generated from `data/mount-dimensions.json`.
