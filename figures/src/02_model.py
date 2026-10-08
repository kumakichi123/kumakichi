import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams["font.family"]="WenQuanYi Zen Hei"; plt.rcParams["axes.unicode_minus"]=False
RED,BLUE,GRAY="#d6453d","#2f6db5","#555"
fig,axs=plt.subplots(1,3,figsize=(18,6.4))

# (a) 実空間
ax=axs[0]; ax.set_xlim(-1.2,3.2); ax.set_ylim(-2,2); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Rectangle((-1.2,-2),1.2,4,color="#dddddd")); ax.add_patch(Rectangle((0,-2),3.2,4,color="#fdf3e1"))
ax.plot([0,0],[-2,2],color="k",lw=3)
ax.text(-0.6,1.5,"真空\n（粒子は\n入れない）",ha="center",va="top",fontsize=12)
ax.text(1.6,1.6,"d 波超伝導体（x > 0）",ha="center",fontsize=13)
ax.text(0.08,-1.85,"表面 x = 0\n（鏡面反射の壁）",fontsize=11)
ax.annotate("",xy=(1.2,0.5),xytext=(0,0.5),arrowprops=dict(arrowstyle="-|>",lw=2))
ax.text(1.25,0.45,"x（表面の法線）",fontsize=11,va="center")
a=np.deg2rad(45); o=np.array([2.0,-1.1])
for ang,l in ((a,"a 軸"),(a+np.pi/2,"b 軸")):
    d=0.8*np.array([np.cos(ang),np.sin(ang)])
    ax.annotate("",xy=o+d,xytext=o,arrowprops=dict(arrowstyle="-|>",lw=2,color="#8a5a00"))
    ax.text(*(o+1.12*d),l,fontsize=11,color="#8a5a00",ha="center",va="center")
ax.plot([o[0],o[0]+0.9],[o[1],o[1]],color="#8a5a00",ls=":")
t=np.linspace(0,a,30); ax.plot(o[0]+0.45*np.cos(t),o[1]+0.45*np.sin(t),color="#8a5a00")
ax.text(o[0]+0.55,o[1]+0.15,"α",fontsize=13,color="#8a5a00")
ax.set_title("(a) 実空間：半無限の超伝導体",fontsize=14,fontweight="bold")

def kpanel(ax,alpha,title,note):
    th=np.linspace(0,2*np.pi,1441); D=np.cos(2*(th-alpha)); rr=1+0.6*np.abs(D)**2
    ax.plot(np.cos(th),np.sin(th),color=GRAY,ls="--",lw=1)
    for s,c in((1,RED),(-1,BLUE)):
        m=np.where(np.sign(D)==s,1.0,np.nan); ax.plot(rr*np.cos(th)*m,rr*np.sin(th)*m,color=c,lw=2.5)
    ti,to=np.deg2rad(155),np.deg2rad(25)
    for tt,lab in((ti,"入射 k"),(to,"反射 k")):
        ax.annotate("",xy=(np.cos(tt),np.sin(tt)),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",lw=2))
        d=np.cos(2*(tt-alpha)); c=RED if d>0 else BLUE
        ax.text(1.85*np.cos(tt),1.85*np.sin(tt),f"{lab}\nΔ{'＞' if d>0 else '＜'}0",ha="center",va="center",fontsize=12,color=c)
    ax.plot([np.cos(ti),np.cos(to)],[np.sin(ti),np.sin(to)],color=GRAY,ls=":",lw=1.5)
    ax.annotate("",xy=(0.7,-2.0),xytext=(0,-2.0),arrowprops=dict(arrowstyle="-|>",color=GRAY)); ax.text(0.75,-2.0,"kx",va="center",color=GRAY)
    ax.annotate("",xy=(-1.9,-1.3),xytext=(-1.9,-2.0),arrowprops=dict(arrowstyle="-|>",color=GRAY)); ax.text(-1.9,-1.2,"ky",ha="center",color=GRAY)
    ax.text(0,-2.55,note,ha="center",fontsize=12)
    ax.set_title(title,fontsize=14,fontweight="bold"); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-2.4,2.4); ax.set_ylim(-2.9,2.6)
kpanel(axs[1],0,"(b) α = 0°：(100) 表面","反射の前後で Δ は同じ符号")
kpanel(axs[2],np.pi/4,"(c) α = 45°：(110) 表面","反射の前後で Δ の符号が反転")
fig.text(0.67,0.02,"破線の円＝フェルミ面（2 次元・円形と仮定）。外側の花びらの長さ＝|Δ|、色＝符号（赤＋、青－）。反射では ky が保存し、kx だけ反転する。",ha="center",fontsize=11,color=GRAY)
plt.tight_layout(w_pad=3,rect=(0,0.05,1,0.95))
plt.savefig("/home/user/kumakichi/figures/02_model.png",dpi=130)
