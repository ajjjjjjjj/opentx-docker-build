#!/usr/bin/env python

languages = (
    "en",
    "fr",
    "se",
    "it",
    "cz",
    "de",
    "pt",
    "es",
    "pl",
    "nl"
)

tts_languages = {
    "en",
    "fr",
    "it",
    "cz",
    "de",
    "pt"
}

options_i6x = {
    "heli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "gvars": ("GVARS", "YES", "NO"),
    "lua": ("LUA", "NO", "NO_MODEL_SCRIPTS"),
    "nographics": ("GRAPHICS", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "imperial": ("UNITS", "IMPERIAL", "METRIC"),
    "multimodule": ("MULTIMODULE", "NO", "YES"),
    # "sqt5font": ("FONT", "SQT5", None),
}

options_taranis_x9lite = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "autoupdate": ("AUTOUPDATE", "YES", None),
    "sqt5font": ("FONT", "SQT5", None),
    "noras": ("RAS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "internalpxx1": ("INTERNAL_MODULE_PXX1", "YES", "NO"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}
