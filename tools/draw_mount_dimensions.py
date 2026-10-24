"""Generate the dimension sheet from revision 02 parameters (millimeters)."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
r=Path(__file__).resolve().parents[1]
p=json.loads((r/'data/mount-dimensions.json').read_text())
A=p['base_width'];L=p['clip_length'];B=p['base_thickness'];W=p['lamp_width'];i=p['inner_wall_spacing']/2;o=i+p['wall_thickness'];t=W/2-p['tongue_entry_per_side'];z0=p['tongue_lower_face_height'];z1=z0+p['tongue_thickness'];h=p['screw_center_spacing']/2
ink='#203950';blue='#176dc0';orange='#d8771f';fill='#a8d9ed'
fig=plt.figure(figsize=(15,10),facecolor='white')
fig.text(.045,.955,'V-102 | Revision 02 mount dimensions',fontsize=24,weight='bold',color=ink)
fig.text(.045,.918,'All dimensions in mm. Owner-reported successful fit on one lamp. Digital geometry shown below.',fontsize=12,color=ink)
def dim(ax,a,b,label,offset=(0,0),color=blue):
 ax.annotate('',xy=a,xytext=b,arrowprops=dict(arrowstyle='<->',color=color,lw=1.3,shrinkA=0,shrinkB=0))
 ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='center',fontsize=10,color=color,bbox=dict(facecolor='white',edgecolor='none',pad=1))
def setup(ax,title):
 ax.set_title(title,loc='left',fontsize=14,weight='bold',color=ink,pad=16);ax.set_aspect('equal');ax.axis('off')
ax=fig.add_axes([.045,.49,.60,.36]);setup(ax,'TOP VIEW | screw mounting plate')
ax.add_patch(Rectangle((-A/2,0),A,L,fc=fill,ec=ink,lw=1.5))
for side in [-1,1]:
 ax.add_patch(Rectangle(((t if side>0 else -o),0),o-t,L,fc='#6bacc7',ec=ink))
 ax.add_patch(Circle((side*h,L/2),p['screw_hole_diameter']/2,fc='white',ec=ink))
 ax.plot([side*h,side*h],[-3,L/2],color=blue,lw=.6)
dim(ax,(-A/2,-3),(A/2,-3),'48.0 base width',(0,-1.2))
dim(ax,(-h,L+3),(h,L+3),'38.45 screw centers',(0,1.3))
dim(ax,(A/2+3,0),(A/2+3,L),'24.0',(2.3,0))
ax.annotate('2 x diameter 4.5',xy=(-h+1.5,L/2+1.5),xytext=(-24,21),fontsize=10,color=ink,arrowprops=dict(arrowstyle='->',color=ink))
ax.set(xlim=(-28,32),ylim=(-7,31))
ax=fig.add_axes([.045,.16,.60,.23]);setup(ax,'END SECTION | tongues face inward')
points=[[-A/2,0],[A/2,0],[A/2,B],[o,B],[o,z1],[t,z1],[t,z0],[i,z0],[i,B],[-i,B],[-i,z0],[-t,z0],[-t,z1],[-o,z1],[-o,B],[-A/2,B]]
ax.add_patch(Polygon(points,fc=fill,ec=ink,lw=1.5))
for x in [-i,i]:ax.plot([x,x],[z1,10],color=blue,lw=.6)
dim(ax,(-i,9),(i,9),'23.1 inner wall spacing',(0,1.1))
dim(ax,(-t,5),(t,5),'22.1 between tips',(0,0))
dim(ax,(-26,0),(-26,B),'3.0',(-1.4,0))
ax.set(xlim=(-30,32),ylim=(-2,12))
ax=fig.add_axes([.70,.50,.25,.32]);setup(ax,'RIGHT TONGUE DETAIL')
ax.add_patch(Polygon([[i,3],[o,3],[o,z1],[t,z1],[t,z0],[i,z0]],fc=fill,ec=ink,lw=1.5))
ax.plot([W/2,W/2],[5.7,8.2],ls='--',color=orange,lw=1)
dim(ax,(t,7.3),(W/2,7.3),'0.7 nominal entry',(0,.23),orange)
dim(ax,(t,5.8),(i,5.8),'0.5 projection',(0,-.3))
dim(ax,(10.5,z0),(10.5,z1),'0.6',(-.28,0))
ax.text(12.0,7.9,'Dashed: nominal\nlamp outer side',color=orange,fontsize=9)
ax.set(xlim=(9.6,14.7),ylim=(4.4,8.9))
fig.text(.70,.38,'Height references',fontsize=13,weight='bold',color=ink)
fig.text(.70,.345,'Base outside face: 0.0\nTongue lower face: 6.2\nTongue upper face: 6.8\nSide wall thickness: 2.4',fontsize=11,color=ink,linespacing=1.7,va='top')
fig.text(.045,.065,'The 0.7 entry is measured from the nominal 23.5-wide lamp envelope, not from the clip wall.',fontsize=11,color=ink)
fig.text(.045,.035,'Groove depth remains uncertain; this diagram specifies the mount, not the lamp metal section or a load rating.',fontsize=11,color=ink)
for extension in ['png','svg']:
 fig.savefig(r/f'images/mount-dimensions.{extension}',dpi=180,facecolor='white')
