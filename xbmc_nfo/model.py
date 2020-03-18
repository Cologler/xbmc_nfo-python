# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from xmlproxy import (
    et,
    text_property, text_list_property,
    element_property, element_list_property,
    tostring,
)

class Set(et.Element):
    name = text_property('name')
    overview =text_property('overview')

class Actor(et.Element):
    name = text_property('name')
    role = text_property('role')
    thumb = text_property('thumb')
    profile = text_property('profile')

class Movie(et.Element):
    def __init__(self):
        super().__init__('movie')

    id: str = None

    title: str = text_property('title')
    sorttitle: str = text_property('sorttitle')
    originaltitle: str = text_property('originaltitle')
    tagline: str = text_property('tagline')

    outline: str = text_property('outline')
    plot: str = text_property('plot')
    runtime: str = text_property('runtime')

    year: str = text_property('year')
    releasedate: str = text_property('releasedate')
    premiered: str = text_property('premiered')

    poster: str = text_property('poster')
    cover: str = text_property('cover')
    tagline: str = text_property('tagline')

    actor = element_list_property('actor', Actor)

    # classify
    genre = text_list_property('genre')
    tags = text_list_property('tag') # cannot use tag direct
    set = element_list_property('set', Set);

    # from
    country = text_list_property('country')
    studio = text_list_property('studio')
    website = text_property('website')

    def tostring(self):
        return tostring(self)
