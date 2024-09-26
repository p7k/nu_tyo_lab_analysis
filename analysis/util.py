def dedup_trace_legends():
    names = set()
    return lambda trace: trace.update(showlegend=False) if (trace.name in names) else names.add(trace.name)