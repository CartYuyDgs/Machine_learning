import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

#print(np.linspace(4,-4,100))

def nomal_distribution():
    plt.figure()
    plt.plot(np.linspace(4,-4,100),
             stats.norm.pdf(np.linspace(4,-4,100))/np.max(stats.norm.pdf(np.linspace(3,-3,100))))
    plt.fill_between(np.linspace(4,-4,100),
             stats.norm.pdf(np.linspace(4,-4,100))/np.max(stats.norm.pdf(np.linspace(3,-3,100))),
                     alpha = 0.15)
    plt.plot(np.linspace(4,-4,100),
             stats.norm.cdf(np.linspace(4,-4,100)))


    print(np.max(stats.norm.pdf(np.linspace(3,-3,100))))

    # LEGEND
    plt.text(x=-1.5, y=.7, s="pdf (normed)", rotation=65, alpha=.75, weight="bold", color="#008fd5")
    plt.text(x=-.4, y=.5, s="cdf", rotation=55, alpha=.75, weight="bold", color="#fc4f30")

    # TICKS
    plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
    plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

    # TITLE
    plt.title(s = "Normal Distribution - Overview",
                   fontsize = 26, weight = 'bold', alpha = .75)
    # plt.text(x = -5, y = 1.1,
    # #          s = 'Depicted below are the normed probability density function (pdf) and the cumulative density\nfunction (cdf) of a normally distributed random variable $ y \sim \mathcal{N}(\mu,\sigma) $, given $ \mu = 0 $ and $ \sigma = 1$.',
    #          fontsize = 19, alpha = .85)

    plt.show()

def nomal_loc():
    plt.figure()
    plt.plot(np.linspace(6,-4,100),
             stats.norm.pdf(np.linspace(6,-4,100),loc = 2))
    plt.fill_between(np.linspace(6,-4,100),stats.norm.pdf(np.linspace(6,-4,100),loc = 2),alpha=0.15)

    plt.plot(np.linspace(4, -4, 100),
             stats.norm.pdf(np.linspace(4, -4, 100)))
    plt.fill_between(np.linspace(4, -4, 100), stats.norm.pdf(np.linspace(4, -4, 100)), alpha=0.15)

    plt.plot(np.linspace(4, -6, 100),
             stats.norm.pdf(np.linspace(4, -6, 100), loc=-2))
    plt.fill_between(np.linspace(4, -6, 100), stats.norm.pdf(np.linspace(4, -6, 100), loc=-2), alpha=0.15)

    plt.text(x=-2, y=.25, s="loc=0", rotation=65, alpha=.75, weight="bold", color="#008fd5")
    plt.text(x=-4, y=.25, s="loc=-2", rotation=65, alpha=.75, weight="bold", color="#008fd5")
    plt.text(x=0.4, y=.25, s="loc=2", rotation=65, alpha=.75, weight="bold", color="#008fd5")

    plt.show()

def nomal_scale():
    plt.figure()
    plt.plot(np.linspace(6, -4, 100),
             stats.norm.pdf(np.linspace(6, -4, 100), scale=2))
    plt.fill_between(np.linspace(6, -4, 100), stats.norm.pdf(np.linspace(6, -4, 100), scale=2), alpha=0.15)

    plt.plot(np.linspace(4, -4, 100),
             stats.norm.pdf(np.linspace(4, -4, 100)))
    plt.fill_between(np.linspace(4, -4, 100), stats.norm.pdf(np.linspace(4, -4, 100)), alpha=0.15)

    plt.plot(np.linspace(4, -6, 100),
             stats.norm.pdf(np.linspace(4, -6, 100), scale=0.5))
    plt.fill_between(np.linspace(4, -6, 100), stats.norm.pdf(np.linspace(4, -6, 100), scale=0.5), alpha=0.15)
    plt.text(x=-1.25, y=.3, s="$ \sigma = 1$", rotation=51, alpha=.75, weight="bold", color="#008fd5")
    plt.text(x=-2.5, y=.13, s="$ \sigma = 2$", rotation=11, alpha=.75, weight="bold", color="#fc4f30")
    plt.text(x=-0.75, y=.55, s="$ \sigma = 0.5$", rotation=75, alpha=.75, weight="bold", color="#e5ae38")
    plt.show()


if __name__ == '__main__':
    # nomal_loc()
    nomal_scale()