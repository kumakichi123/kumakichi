import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
plt.rcParams["font.family"]="WenQuanYi Zen Hei"
plt.rcParams["axes.unicode_minus"]=False
RED,BLUE,GRAY="#d6453d","#2f6db5","#555"

fig,axs=plt.subplots(1,4,figsize=(18,5.6))
def polar_gap(ax,f,title):
    th=np.linspace(0,2*np.pi,721); r=f(th)
    ax.add_patch(plt.Circle((0,0),1,fill=False,ls="--",color=GRAY,lw=1))
    rr=1+0.6*np.abs(r); x,y=rr*np.cos(th),rr*np.sin(th)
    for sgn,c in((1,RED),(-1,BLUE)):
        m=np.where(np.sign(r)==sgn,1.0,np.nan); ax.fill(np.r_[np.cos(th)],np.r_[np.sin(th)],color="none")
        ax.plot(x*m,y*m,color=c,lw=2.5)
    ax.set_title(title,fontsize=13); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.9,1.9); ax.set_ylim(-1.9,1.9)

# ① 問い
ax=axs[0]; ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.set_title("① 問い：ギャップに符号はあるか",fontsize=14,fontweight="bold")
for cx,f,lab in((0.25,lambda t:np.ones_like(t),"s 波\n（全方向で＋）"),(0.75,lambda t:np.cos(2*t),"d 波\n（＋と－が交互）")):
    th=np.linspace(0,2*np.pi,721); r=f(th); rr=0.04+0.16*np.abs(r)
    for sgn,c in((1,RED),(-1,BLUE)):
        m=np.where(np.sign(r)==sgn,1.0,np.nan)
        ax.plot(cx+rr*np.cos(th)*m,0.6+rr*np.sin(th)*m,color=c,lw=2.5)
    ax.text(cx,0.3,lab,ha="center",va="top",fontsize=12)
ax.text(0.5,0.05,"大きさだけ測っても区別しにくい",ha="center",fontsize=11,color=GRAY)
ax.text(0.04,0.93,"赤＝＋　青＝－",fontsize=10)

# ② 設定
ax=axs[1]; ax.set_xlim(-0.3,2); ax.set_ylim(-1.2,1.2); ax.axis("off"); ax.set_aspect("equal")
ax.set_title("② 設定：表面のある d 波超伝導体",fontsize=14,fontweight="bold")
ax.add_patch(Rectangle((-0.3,-1.2),0.3,2.4,color="#bbbbbb"))
ax.add_patch(Rectangle((0,-1.2),2,2.4,color="#fdf3e1"))
ax.text(-0.15,0,"表面\n（壁）",ha="center",va="center",fontsize=11,rotation=90)
ax.text(1.0,1.0,"超伝導体",ha="center",fontsize=12)
ax.annotate("",xy=(0,0.15),xytext=(1.3,0.85),arrowprops=dict(arrowstyle="-|>",color="k",lw=2))
ax.annotate("",xy=(1.3,-0.55),xytext=(0,0.15),arrowprops=dict(arrowstyle="-|>",color="k",lw=2))
ax.text(0.85,0.75,"入射",fontsize=11); ax.text(0.85,-0.55,"反射",fontsize=11)
ax.text(1.0,-1.05,"準粒子が表面で鏡のように跳ね返る",ha="center",fontsize=11,color=GRAY)

# ③ 鍵
ax=axs[2]
th=np.linspace(0,2*np.pi,721); r=-np.sin(2*th); rr=0.1+0.9*np.abs(r)
for sgn,c in((1,RED),(-1,BLUE)):
    m=np.where(np.sign(r)==sgn,1.0,np.nan); ax.plot(rr*np.cos(th)*m,rr*np.sin(th)*m,color=c,lw=2.5)
a_in,a_out=np.deg2rad(150),np.deg2rad(30)
for a,c,l in((a_in,RED,"入射の向き\nΔ＞0"),(a_out,BLUE,"反射の向き\nΔ＜0")):
    ax.annotate("",xy=(0.9*np.cos(a),0.9*np.sin(a)),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",color="k",lw=2))
    ax.text(1.25*np.cos(a),1.25*np.sin(a)+0.05,l,ha="center",fontsize=11,color=c)
ax.axvline(-1.45,color="#999",lw=6)
ax.set_title("③ 鍵：反射で Δ の符号が反転",fontsize=14,fontweight="bold")
ax.text(0,-1.5,"表面の法線を [110] に取ったとき\nどの入射角でも符号が反転",ha="center",fontsize=11,color=GRAY)
ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.6,1.6); ax.set_ylim(-1.8,1.6)

# ④ 結果
ax=axs[3]; E=np.linspace(-2,2,800); g=0.04
Ns=np.real(np.abs(E+1j*g)/np.sqrt((E+1j*g)**2-1+0j)); Ns=np.abs(Ns)
Nd=0.55*np.abs(E)+0.15+2.6/(1+(E/0.05)**2)
ax.plot(E,np.clip(Ns,0,3.2),color=GRAY,lw=2,label="s 波：E=0 付近に状態なし")
ax.plot(E,np.clip(Nd,0,3.2),color=RED,lw=2.5,label="d 波 (110) 表面：E=0 に鋭いピーク")
ax.set_xlabel("エネルギー E（単位 Δ，E=0 がフェルミ準位）",fontsize=11); ax.set_ylabel("表面の状態密度（模式）",fontsize=11)
ax.set_yticks([]); ax.set_ylim(0,3.4); ax.legend(fontsize=10,loc="upper center",frameon=False)
ax.set_title("④ 結果：ギャップの真ん中に状態",fontsize=14,fontweight="bold")
fig.text(0.875,0.03,"→ トンネル分光でゼロバイアスのピークとして見えるはず",ha="center",fontsize=11,color=GRAY)
for i in range(3):
    fig.add_artist(FancyArrowPatch((0.25*(i+1)-0.022,0.55),(0.25*(i+1)-0.002,0.55),transform=fig.transFigure,arrowstyle="-|>",mutation_scale=25,color="k"))
plt.tight_layout(w_pad=5,rect=(0,0.06,1,1))
plt.savefig("/home/user/kumakichi/figures/01_overview.png",dpi=130)
