from calcul import Calcul
from mpl_toolkits.axisartist.axislines import AxesZero
import matplotlib.pyplot as plt
import numpy as np 



object1 = Calcul()
object1.recup_nb()
object1.delta()
object1.determin_x()
object1.alpha_beta()

# object1.delta()
x = np.linspace(-10, 10, 1000)
y = (object1.a* x**2) + (object1.b*x) + object1.c
fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)
# fig.set_size_inches(20, 40)
# ax.axis["x"].set_axislabel_direction("-")
for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)
for direction in [ "right", "bottom", "left", "top" ]:
    # hides borders
    ax.axis[direction].set_visible(False)
ax.plot(x, y, linewidth = 2)
ax.set_title("Graphique", loc = ("left"))
# ax.set_xlabel("X", loc = "left")
# ax.set_ylabel("Y", loc = "bottom")
ax.set_xlim(-7.1, 10)
ax.set_ylim(-10, 15)
plt.xticks(np.arange(min(x), max(x)+1, 1))
ax.plot(object1.alpha,object1.beta, marker = "+", label = "(α, β)", color = "red")
ax.plot(0,object1.c, marker = "+", label = f"C(0,{object1.c})", color = "green")
if object1.delta >0:
    ax.plot(object1.x_reelle_1,0, marker = "x", label = "(x1)", color = "blue")
    ax.plot(object1.x_reelle_2,0, marker = "x", label = "(x2)", color = "blue")
    plt.axvline(x = object1.x_reelle_1, color = "grey", linestyle = "-.")
    plt.axvline(x = object1.x_reelle_2, color = "grey", linestyle = ":")
elif object1.delta == 0:
    ax.plot(0,object1.x_double, marker = "+", label = "(x1)", color = "blue")
else:
    plt.text( 10, -10, object1.result_delta_n,
            fontsize = 10, color = 'red', horizontalalignment=  "right",)


plt.grid(linewidth = 1)
plt.legend()
fm = plt.get_current_fig_manager()
fm.window.showMaximized()
plt.show()

