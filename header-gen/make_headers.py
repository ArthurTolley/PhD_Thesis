from pycbc.waveform import get_td_waveform
from pycbc.types import TimeSeries
import matplotlib.pyplot as plt
import numpy as np
import os

# For the science style, consistent with the thesis
import scienceplots
plt.style.use('science')

# end is number of pages in thesis
for m in range(1,250):
    template, hc = get_td_waveform(approximant="IMRPhenomXAS",
                            mass1=m,
                            mass2=m,
                            delta_t=1/2048.0,
                            f_lower=20)

    # Convert template to a numpy array before normalizing
    template_times = np.array(template.sample_times)
    template_numpy = np.array(template)
    template_centered = template_numpy - np.mean(template_numpy)

    # Normalize the waveform to the range [-1, 1]
    template_normalized = template_centered / np.max(np.abs(template_centered))

    fig, axis = plt.subplots(figsize=(2, 1))

    axis.tick_params(
        axis='both', which='both',
        bottom=False, top=False,
        left=False, right=False,
        labelbottom=False, labeltop=False,
        labelleft=False, labelright=False
    )

    axis.spines['top'].set_visible(False)
    axis.spines['right'].set_visible(False)
    axis.spines['bottom'].set_visible(False)
    axis.spines['left'].set_visible(False)

    y_min, y_max = -1.0, 1.0
    axis.set_ylim([y_min, y_max])

    axis.plot(template_times, template_normalized, color='goldenrod', rasterized=False)
    # Create a directory to store all the header pdfs
    if not os.path.exists('headers'):
        os.makedirs('headers')
    plt.savefig(f'headers/{m}.pdf', bbox_inches='tight')
    plt.close()