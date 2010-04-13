#!/usr/bin/python

import gtk
import pango

quotes = """Excess of joy is harder to bear than any amount of sorrow.
The more one judges, the less one loves.
There is no such thing as a great talent without great will power. 
"""


class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("Pango Example")
        
        label = gtk.Label(quotes)
        gtk.gdk.beep()

        fontdesc = pango.FontDescription("Serif bold 16")
        label.modify_font(fontdesc)

        attlist = pango.AttrList()
        offset = pango.AttrForeground(65535, 0, 0, start_index=30, end_index=40)
        attlist.insert(offset)
        att = pango.AttrStrikethrough(True, start_index=0, end_index=10)
        attlist.insert(att)

        gtk.Label.set_attributes(label, attlist)
        gtk.Label.set_justify(label, gtk.JUSTIFY_CENTER)

        fix = gtk.Fixed()

        fix.put(label, 5, 5)
        
        self.add(fix)
        self.set_position(gtk.WIN_POS_CENTER)
        self.show_all()

PyApp()
gtk.main()
