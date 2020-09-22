DESCRIPTION = """Convert between Eclipse restart files ROFF grid format.

This forward model uses the script ``convert_grid_format`` from subscript.

Destination directory must exist.

One file will be written for each of the requested parameters, the example
given below will produce the files::

    share/results/grids/eclgrid--sgas--20200101.roff
    share/results/grids/eclgrid--soil--20200101.roff

if the file ``dates.txt`` contains only the line::

    20200101
"""

CATEGORY = "utility.eclipse"

EXAMPLES = "FORWARD_MODEL ECLRST2ROFF(<ECLROOT>=<ECLBASE>, <OUTPUT>=share/results/grids/eclgrid, <PROP>=SGAS:SWAT, <DATES>=dates.txt)"  # noqa
