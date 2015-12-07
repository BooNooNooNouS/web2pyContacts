# -*- coding: utf-8 -*-

db.define_table('employees',
                Field('name'),
                Field('phone'),
                Field('email'),
                Field('age', 'integer'),
               )
