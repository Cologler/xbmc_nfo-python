# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from xbmc_nfo import Movie

def test_movie_title():
    movie = Movie()
    movie.title = 'abc'
    assert movie.tostring() == "<movie><title>abc</title></movie>"

    # set agains
    movie.title = '123'
    assert movie.tostring() == "<movie><title>123</title></movie>"

def test_movie_actor():
    movie = Movie()
    actor = movie.actor.new_sub()
    actor.name = 'abc'
    assert movie.tostring() == "<movie><actor><name>abc</name></actor></movie>"
    actor.role = 'sss'
    assert movie.tostring() == "<movie><actor><name>abc</name><role>sss</role></actor></movie>"
