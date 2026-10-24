from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d

OUT=Path(__file__).resolve().parents[1]/'images'
blue='#176dc0'; orange='#d8771f'; ink='#203950'; muted='#556b7e'
fig=plt.figure(figsize=(15,10),facecolor='#f7f9fc')
fig.text(.055,.95,'V-102 | Lamp measurement reference',fontsize=25,fontweight='bold',color=ink)
fig.text(.055,.915,'Owner measurements: A 1150 | B 23.5 | C 14 | H 1114 mm. Mass: 120 g.',fontsize=14,color=muted)
fig.text(.055,.88,'Schematic only: groove shape and proportions are illustrative, not a manufacturer drawing.',fontsize=11,color=muted)

class Arrow3D(FancyArrowPatch):
 def __init__(self,a,b,**kw):
  super().__init__((0,0),(0,0),**kw);self.a=a;self.b=b
 def do_3d_projection(self,renderer=None):
  xs,ys,zs=proj3d.proj_transform(*np.array([self.a,self.b]).T,self.axes.get_proj())
  self.set_positions((xs[0],ys[0]),(xs[1],ys[1]));return min(zs)

ax=fig.add_axes([.035,.405,.57,.435],projection='3d',computed_zorder=False)
ax.set_facecolor('#f7f9fc')
profile=[(-16,8),(16,8),(16,14),(12,14),(12,16),(16,16),(16,22),(-16,22),(-16,16),(-12,16),(-12,14),(-16,14)]
faces=[];colors=[]
for i in range(len(profile)):
 a=profile[i];b=profile[(i+1)%len(profile)]
 faces.append([(a[0],0,a[1]),(b[0],0,b[1]),(b[0],160,b[1]),(a[0],160,a[1])])
 colors.append('#8495a4' if i in [2,3,8,9] else '#dbe3e9')
faces += [[(x,0,z) for x,z in profile],[(x,160,z) for x,z in profile]]
colors += ['#bdcbd7','#bdcbd7']
poly=Poly3DCollection(faces,facecolors=colors,edgecolors='#6b8295',linewidths=.7,zorder=2)
ax.add_collection3d(poly)
# Schematic diffuser.
xx=np.linspace(-16,16,28);zz=8-7*np.sqrt(np.maximum(0,1-(xx/16)**2))
diff=[]
for i in range(len(xx)-1):
 diff.append([(xx[i],0,zz[i]),(xx[i+1],0,zz[i+1]),(xx[i+1],160,zz[i+1]),(xx[i],160,zz[i])])
diff.append([(x,0,z) for x,z in zip(xx,zz)]+[(16,0,8),(-16,0,8)])
ax.add_collection3d(Poly3DCollection(diff,facecolors='#dceef7',edgecolors='none',zorder=1))
# Highlight groove opening; tongue enters inward from outside.
for z in [14,16]: ax.plot([16.1,16.1],[0,160],[z,z],color=orange,lw=2,zorder=5)
def arrow(a,b,label,at):
 ob=Arrow3D(a,b,arrowstyle='<->',mutation_scale=14,lw=1.6,color=blue,zorder=20,clip_on=False);ax.add_artist(ob)
 ax.text(*at,label,color=blue,fontsize=15,fontweight='bold',zorder=30)
def ext(a,b): ax.plot(*np.array([a,b]).T,color='#94a8b9',lw=.8,zorder=10,clip_on=False)
arrow((27,0,-4),(27,160,-4),'A',(29,76,-5))
ext((16,0,8),(27,0,-4));ext((16,160,8),(27,160,-4))
arrow((-16,-21,29),(16,-21,29),'B',(-1,-28,32))
ext((-16,0,22),(-16,-21,29));ext((16,0,22),(16,-21,29))
arrow((-32,-7,1),(-32,-7,22),'C',(-38,-7,10))
ext((-16,0,1),(-32,-7,1));ext((-16,0,22),(-32,-7,22))
arrow((23,15,32),(23,145,32),'H',(24,77,34))
ax.text(-11,65,24,'Back',fontsize=10,color=ink,zorder=30)
ax.text(25,105,15,'Side groove',fontsize=10,color=orange,zorder=30)
ax.view_init(elev=25,azim=-53);ax.set_proj_type('ortho')
ax.set(xlim=(-35,37),ylim=(-25,167),zlim=(-10,38));ax.set_box_aspect((70,170,57),zoom=1.45);ax.axis('off')

detail=fig.add_axes([.65,.43,.30,.36]);detail.set_facecolor('#f7f9fc')
detail.set_title('One side groove | enlarged schematic',loc='left',fontsize=15,fontweight='bold',color=ink,pad=16)
pp=[(-4,0),(-3,0),(-3,2),(2,2),(2,3),(-2,3),(-2,5),(2,5),(2,8),(-4,8)]
detail.add_patch(Polygon(pp,facecolor='#c9d5df',edgecolor='#637d92',lw=1.5))
detail.plot([-2,2],[3,3],color=orange,lw=3);detail.plot([-2,2],[5,5],color=orange,lw=3)
def dim(a,b,letter,textat):
 detail.annotate('',xy=a,xytext=b,arrowprops=dict(arrowstyle='<->',color=blue,lw=1.6,shrinkA=0,shrinkB=0))
 detail.text(*textat,letter,color=blue,fontweight='bold',fontsize=15,ha='center',va='center')
dim((3.4,3),(3.4,5),'D',(4.25,4))
dim((-2,4),(2,4),'E',(0,4.6))
dim((-5.2,5),(-5.2,8),'F',(-6,6.5))
for z in [5,8]: detail.plot([-5.2,-4],[z,z],color='#94a8b9',lw=.8)
dim((1,2),(1,3),'G',(.9,1.1))
detail.annotate('Tongue enters here',xy=(1.8,4),xytext=(3.1,6.7),color=orange,fontsize=10,
 arrowprops=dict(arrowstyle='->',color=orange,lw=1.3))
detail.text(-3.9,8.45,'Back',color=ink,fontsize=10)
detail.text(-3.8,.8,'Inside',color=muted,fontsize=9)
detail.text(3,.1,'Outside',color=muted,fontsize=9)
detail.set(xlim=(-6.7,6.8),ylim=(-.3,9.2));detail.set_aspect('equal');detail.axis('off')

fig.text(.055,.375,'DIMENSION KEY',fontsize=13,fontweight='bold',color=ink)
items=[
 ('A','Overall length including end caps: 1150 mm.'),
 ('B','Body width between grooved sides: 23.5 mm.'),
 ('C','Overall height including diffuser: 14 mm.'),
 ('H','Continuous usable groove length: 1114 mm.'),
 ('D','Groove opening: approximately 1 mm.'),
 ('E','Groove depth: initially estimated at 0.5 mm or less.'),
 ('F','Back to nearest groove edge: approximately 1 mm.'),
 ('G','Lower groove lip thickness: approximately 3 mm.'),
]
for i,(letter,txt) in enumerate(items):
 col=0 if i<4 else 1;row=i%4;x=.055+col*.49;y=.335-row*.045
 fig.text(x,y,letter,color=blue,fontweight='bold',fontsize=16)
 fig.text(x+.027,y+.001,txt,color=ink,fontsize=10.4)
fig.text(.055,.125,'D, E, F and G are approximate. A successful fit does not establish the actual groove depth.',fontsize=12,fontweight='bold',color=orange)
fig.text(.055,.083,'The owner reports axial entry from the end without removing the caps. Intended location: under a shelf.',fontsize=11,color=muted)
fig.text(.055,.055,'The lamp receives the inward-facing tongues in its grooves; do not reverse the male/female geometry.',fontsize=11,color=muted)
fig.savefig(OUT/'lamp-measurement-map.png',dpi=180,facecolor=fig.get_facecolor())
