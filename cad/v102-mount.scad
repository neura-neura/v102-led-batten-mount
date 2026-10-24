// V-102 shelf mount, revision 02. All dimensions in mm.
// User-reported fit on one lamp; no load or temperature rating.
/* [Fit] */
lamp_width = 23.5;
inner_spacing = 23.1;
tongue_entry = 0.7;
tongue_thickness = 0.6;
tongue_lower_height = 6.2;
/* [Structure] */
wall_thickness = 2.4;
base_thickness = 3;
base_width = 48;
clip_length = 24;
/* [Screws] */
hole_diameter = 4.5;
hole_centers = 38.45;
/* [Export] */
print_orientation = true;
/* [Hidden] */
$fn = 96;
i = inner_spacing/2;
o = i + wall_thickness;
t = lamp_width/2 - tongue_entry;
z0 = tongue_lower_height;
z1 = z0 + tongue_thickness;
assert(t > 0 && i > t, "Tongue projection must be positive.");
assert(z0 > base_thickness && tongue_thickness > 0 && clip_length > 0);
assert(hole_centers/2 - hole_diameter/2 > o, "Hole overlaps side wall.");
assert(hole_centers/2 + hole_diameter/2 < base_width/2, "Hole crosses plate edge.");
module mount() {
    difference() {
        translate([0,clip_length,0]) rotate([90,0,0])
        linear_extrude(clip_length)
        polygon([[-base_width/2,0],[base_width/2,0],
            [base_width/2,base_thickness],[o,base_thickness],
            [o,z1],[t,z1],[t,z0],[i,z0],[i,base_thickness],
            [-i,base_thickness],[-i,z0],[-t,z0],[-t,z1],
            [-o,z1],[-o,base_thickness],[-base_width/2,base_thickness]]);
        for (x=[-hole_centers/2,hole_centers/2])
            translate([x,clip_length/2,-1])
                cylinder(d=hole_diameter,h=base_thickness+2);
    }
}
if(print_orientation) rotate([90,0,0]) mount(); else mount();
