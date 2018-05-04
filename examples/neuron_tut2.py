#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neurodamus import Cell
from neurodamus import CurrentSource
from neurodamus import Neuron
from neurodamus.synapses import ExpSyn, NetStim
from os import path

MORPHO = path.join(path.dirname(__file__), "..", "tests/morphology/C060114A7.asc")


def test_tut2():
    c = Cell(0, MORPHO)
    print("The morphology {} basal, {} apical, {} axonal sections.".format(
        len(c.dendrites), len(c.apical_dendrites), len(c.axons)))

    for sec in c.all:
        sec.nseg = 1 + 2 * int(sec.L / 40)
        sec.cm = 1
        sec.Ra = 100

    hh = Cell.Mechanisms.mk_HH(gkbar=.0, gnabar=.0, el=-70)
    hh.apply(c.all)
    hh.gkbar = 0.01
    hh.gnabar = 0.2
    hh.apply(c.soma)
    hh.gnabar = 0.25
    hh.apply(c.axons)

    clamp = CurrentSource.Constant(0.5, 200, 10).attach_to(c.soma)
    Neuron.run_sim(300, c.soma, v_init=-70).plot()

    # Part 2
    clamp.detach()

    stim = NetStim(5, 5, 20, 0)

    for sect in c.dendrites:
        sr = ExpSyn(sect(0.5))
        stim.connect_to(sr, weight=0.001)

    Neuron.run_sim(80, c.soma, v_init=-70).plot()

    # Alternative
    # # --------
    # for sr in ExpSyn().create_on(*c.dendrites):
    #     stim.connect_to(sr, weight=0.001)


if __name__ == "__main__":
    test_tut2()
