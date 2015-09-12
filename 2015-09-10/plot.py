import numpy as np
import matplotlib.pyplot as plt


def main():
    corePeakFlops = 120e9
    corePeakMemory = 59e9

    phiPeakFlops = 2141e9
    phiPeakMemory = 59e9

    step = np.arange(0, 2048, 0.1)

    coreMaxFlops = [min(corePeakFlops, corePeakMemory * s) for s in step]
    phiMaxFlops = [min(phiPeakFlops, phiPeakMemory * s) for s in step]

    plt.loglog(step, coreMaxFlops, label='Intel E5-2620 v3 Only')
    plt.loglog(step, phiMaxFlops, label='With Intel Xeon Phi 5110P')

    plt.xlabel("Operational Intensity")
    plt.ylabel("Attainable FLOP/s")
    plt.grid(True)
    plt.legend(loc='best')
    plt.savefig("roofline.pdf")

if __name__ == "__main__":
    main()
