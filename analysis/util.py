#
# graphing and formatting functions
#

def dedup_trace_legends():
    names = set()
    return lambda trace: trace.update(showlegend=False) if (trace.name in names) else names.add(trace.name)


def fmt_strains(strains: dict[str, set[str]]) -> str:
    return ', '.join([f'{strain_id} ({", ".join(alts)})' for strain_id, alts in strains.items()])


#
# math functions and consts
#

# based on .55 g•CDW / (au•OD600/L)
YIELD_OD600_FROM_X_ARG_M = 1.27e4
