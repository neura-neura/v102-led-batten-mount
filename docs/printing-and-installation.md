# Printing and installation

## What was actually confirmed

The project owner reports that revision 02 fits the lamp. The print material, printer, nozzle, layer height, support settings, number of installed clips, and completed mounting arrangement were not supplied. Do not describe any generic slicer settings as the tested profile.

The approximately 120 g lamp mass is a reference measurement, not a rated capacity for the clips. No sustained-load, impact, fatigue, elevated-temperature, or long-term creep tests were performed or reported.

## Print orientation

The supplied mount STLs are rotated onto the end section of the mount. In the slicer the footprint is 48 × 6.8 mm and the 24 mm length runs vertically. This makes the tongue profile repeat along the print height. Check bed adhesion and add a brim if your printer needs it.

Inspect the layer preview: the 0.6 mm tongues must print as continuous material. Use your printer's established dimensional settings and choose material based on the measured operating temperature and its own technical data. This project does not prescribe an untested permanent-installation material or print profile.

Print one sample first. Do not scale the whole STL to adjust the groove fit; edit inner spacing, entry, or tongue thickness instead.

## Mechanical installation

1. Disconnect the lamp and support it independently while checking fit.
2. Feed the clip from an accessible end so both tongues enter the side grooves. Avoid forcing it over the lamp as a snap-on clip.
3. Verify that both sides remain engaged, the diffuser is clear, and the screw wings do not collide with the casing.
4. Mark and fasten the wings to the shelf using suitable hardware. Keep the lamp supported during fastening; do not use screws to pull a tight clip into place.
5. Check the installed arrangement through the lamp's operating temperature range before relying on it unattended.

Each mount uses two Ø4.5 mm holes, 38.45 mm apart. Flat bearing screw heads with suitable washers distribute load across the wings. Check that the chosen head/washer clears the side walls and stays on the plate; an outside washer diameter of 8.5 mm or less was the original design target. Shelf thickness and material were not supplied, so screw length and anchor choice are intentionally unspecified. Never drill or screw into the lamp casing.

Three mounts centered approximately at 150, 575, and 1000 mm from one end were proposed for the 1150 mm lamp. These positions and the clip count were not reported as tested, and are not a result of a casing-deflection calculation. Adjust them to unobstructed groove sections and the actual shelf.

## Axial retention

A sliding mount may still allow the lamp to slide along its axis. The separate [experimental stop](../stl/experimental/axial-stop-untested.stl) is intended as a surface-mounted barrier against a rigid end-cap face. It is **not physically validated**, and the end caps were not dimensioned.

The stop has a 48 × 12 × 3 mm base, a 32 mm wide × 3 mm thick × 12 mm high barrier, and two Ø3.5 mm holes. Two stops, one at each end, were proposed. Confirm actual contact with rigid end-cap surfaces and clearance from cables/connectors before using them. Stops do not protect against tongue breakage or loss of groove engagement.

## Known uncertainty

The groove opening, depth, lip thickness, and position were estimated by the owner. In particular, the initial depth estimate (0.5 mm or less) does not match the final 0.7 mm nominal entry. The reported fit takes precedence as practical evidence for that one specimen; it does not resolve the true metal section, printer tolerance, or amount of elastic deflection. Do not force another lamp to match the model.
