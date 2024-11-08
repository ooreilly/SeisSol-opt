"""Plot SeisSol matrix sparsity pattern
"""
import reader
import numpy as np
import matplotlib.pyplot as plt



matrixfile = "data/matrices_56.xml"
pngfile = "plots/kDivMT.png"

D = [0] * 3
Dstr = [""] * 3
nnz = [0] * 3



for i in range(3):
    Dstr[i] = f"kDivMT({i})"
    D[i], nnz[i] = reader.readmatrix(matrixfile, Dstr[i])

title = lambda mat, A, nnz : f"{mat} nnz={nnz} sparsity=%f" % ((A.shape[0] * A.shape[1] - nnz) / (A.shape[0] * A.shape[1]))

fig, axs = plt.subplots(3,1)
fig.set_figheight(18)
fig.set_figwidth(6)
for i in range(3):
    axs[i].set_title(title(Dstr[i], D[i], nnz[i]))
    axs[i].matshow(D[i])

plt.savefig(pngfile, dpi=200)
#plt.show()
