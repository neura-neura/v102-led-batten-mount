// Optional axial stop. Not physically validated with the lamp end caps.
// All dimensions in mm. This stop is not a vertical load support.
base_width=48; base_length=12; base_thickness=3;
stop_width=32; stop_depth=3; stop_height=12;
hole_centers=38.45; hole_diameter=3.5;
print_orientation=true; $fn=96;
module stop(){
    difference(){
        union(){
            translate([-base_width/2,0,0])cube([base_width,base_length,base_thickness]);
            translate([-stop_width/2,0,0])cube([stop_width,stop_depth,stop_height]);
        }
        for(x=[-hole_centers/2,hole_centers/2])
            translate([x,7.5,-1])cylinder(d=hole_diameter,h=base_thickness+2);
    }
}
if(print_orientation)rotate([90,0,0])stop();else stop();
