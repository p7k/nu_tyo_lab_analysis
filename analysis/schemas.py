import pandera as pa


class SakaguchiODSchema(pa.DataFrameModel):
    sample: str = pa.Field(str_length=dict(min_value=1))
    conc_factor: float = pa.Field(ge=0, coerce=True)
    vol_sample_ul: float = pa.Field(ge=0, coerce=True)
    vol_reagentA_ul: float = pa.Field(ge=0, coerce=True)
    vol_reagentB_ul: float = pa.Field(ge=0, coerce=True)
    vol_reagentC_ul: float = pa.Field(ge=0, coerce=True)
    arg_conc_known_ug_ml: float = pa.Field(ge=0, coerce=True, nullable=True)
    od520: float = pa.Field(ge=0, coerce=True)
