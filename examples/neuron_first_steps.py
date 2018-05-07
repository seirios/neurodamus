#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A tutorial based on the Neuron documentation at
https://neuron.yale.edu/neuron/static/docs/neuronpython/firststeps.html#step-2-create-a-cell
"""
from neurodamus import Cell, Neuron
from neurodamus import mechanisms
from neurodamus import synapses

c = Cell.Builder.add_soma(100).create()
mechanisms.PAS().apply(c.soma)

syn = synapses.AlphaSynapse(c.soma(0.5), onset=20, gmax=1)

Neuron.run_sim(40, c.soma(0.5)).plot()
