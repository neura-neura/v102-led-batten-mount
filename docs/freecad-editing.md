# Editing the mount in FreeCAD

The project contains native parametric solids and expressions. It does not require the MCP connection, the rebuilding macro, or extra Python packages to edit. Open `cad/v102-mount.FCStd` in FreeCAD.

## Change a dimension

1. Double-click **DIMENSIONS - double-click to edit** in the document tree.
2. Edit a **green cell in column B**. Use a decimal point, for example `0.65`.
3. Press **Enter**. FreeCAD rebuilds the model automatically.
4. Switch back to the 3D model tab to inspect the result. Use **View → Standard views → Fit all** if necessary.
5. Use **File → Save As** to save a new version while preserving the original.

Blue cells are calculated outputs. Leave their formulas intact. Keep the dimensions table and the final solid in the document.

## All editable cells

| Cell | Parameter | Default, mm | Effect |
| --- | --- | ---: | --- |
| B4 | Lamp width | 23.5 | Reference envelope for tongue entry; change only for a different measured lamp. |
| B5 | Inner wall spacing | 23.1 | Smaller values bring the side walls closer together. |
| B6 | Tongue entry per side | 0.7 | Larger values extend the tips farther into the lamp grooves. |
| B7 | Tongue thickness | 0.6 | Thickness fitting inside the groove opening. |
| B8 | Tongue lower-face height | 6.2 | Height above the outside base face. |
| B9 | Side wall thickness | 2.4 | Thickness of each arm. |
| B10 | Base thickness | 3 | Screw plate thickness. |
| B11 | Overall base width | 48 | Width across the mounting wings. |
| B12 | Clip length | 24 | Length parallel to the lamp. |
| B13 | Hole diameter | 4.5 | Screw clearance. |
| B14 | Hole center spacing | 38.45 | Distance between screws. |

Try B6 = `0.6`, inspect the shortened tongues, and restore `0.7` to return to the confirmed-fit revision.

B5 and B6 are independent in this document. B5 controls the walls while B6 controls the tongue tips relative to the lamp. Changing B5 alone keeps the same nominal tongue entry and adjusts tongue projection to suit.

## Derived dimensions

With lamp width `W`, inner spacing `S`, and entry per side `E`:

- Tongue projection from the clip wall: `E + (S - W) / 2` = **0.5 mm**.
- Tip-to-tip spacing: `W - 2E` = **22.1 mm**.
- Nominal interference per side: `(W - S) / 2` = **0.2 mm**.

Projection must stay positive. Keep wall and tongue thickness positive, tongue lower-face height above the base thickness, and holes fully inside the outer wings. Arbitrary parameter combinations are not guaranteed to produce a usable part. If a feature shows an error or disappears, undo the last change and inspect the dimensions.

## Export for printing

1. Return to the 3D view.
2. Select **FINAL MOUNT - select to export** in the tree. Select only that final object.
3. Choose **File → Export** and **STL Mesh (*.stl)**.
4. Open it in your slicer at 100% scale.
5. Rotate it to match the supplied STL's end-on orientation: the 24 mm lamp-axis length should point vertically. Inspect the thin tongues in the layer preview.

Manual export preserves the design orientation (48 × 24 × 6.8 mm). The supplied print STL is rotated 90° about X (48 × 6.8 × 24 mm). Do not globally scale the model to fix a local fit problem.

## Save and rebuild are different

Saving the `.FCStd` file preserves your spreadsheet edits. Running `tools/build_freecad.FCMacro` creates a fresh project from the default values embedded in the macro and writes the standard output filenames. Back up customized files before running it. The macro leaves `stl/v102-mount-r02-confirmed-fit.stl` untouched.

FreeCAD's native project is the preferred editable original; STEP retains solid geometry but does not preserve the spreadsheet feature history, and STL is a triangle mesh.
