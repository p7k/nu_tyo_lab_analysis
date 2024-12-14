from datetime import date, time

import plotly
import more_itertools as mit
from pydantic import BaseModel
from IPython.display import display, Javascript

# mathjax 3.2.1 | seems to work | checked out via github
MATHJAX_JS = '/Users/pasha/src.ext/mathjax/es5/tex-svg-full.js'


class Meta(BaseModel):
    id: str
    title: str
    date: date
    strains: dict[str, list[str]]
    time: time = None


#
# graphing and formatting functions
#

def nb_setup_plotly(template: str = 'plotly_white'):
    nb_setup_mathjax()
    plotly.io.templates.default = template


def nb_setup_mathjax():
    plotly.offline.init_notebook_mode()
    display(Javascript(filename=MATHJAX_JS))
    plotly.io.kaleido.scope.mathjax = f'file://{MATHJAX_JS}'


def dedup_trace_legends():
    names = set()
    return lambda trace: trace.update(showlegend=False) if (trace.name in names) else names.add(trace.name)


def mk_title(title: str, meta: Meta, tex=True) -> str:
    preamb = f'{meta.id} | {meta.date}'
    if tex:
        ret_tex = r'$\textrm{' + preamb.replace('_', '\_') + r'}\textrm{ | }' + title.replace('$', '') + r'$'
        return ret_tex
    return preamb + ' | ' + title


def fmt_strain(strain_id: str, alts: set[str]) -> str:
    return f'{strain_id}: [{", ".join(mit.unique_everseen(alts)) if alts else "wild type"}]'


def fmt_strains(strains: dict[str, set[str]], sep: str = ' | ') -> str:
    return sep.join(fmt_strain(strain_id, alts) for strain_id, alts in strains.items())


#
# math functions and consts
#

# based on .55 g•CDW / (au•OD600/L)
YIELD_OD600_FROM_X_ARG_M = 1.27e4
