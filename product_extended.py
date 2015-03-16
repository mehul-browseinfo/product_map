# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2013-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp


class product_template(osv.osv):
    _inherit = "product.template"

    _columns = {
        'start_date': fields.date('Start Date'),
        'end_date': fields.date('End Date'),
        'qty_warehouse1':fields.float('Warehouse1'),
        'qty_warehouse2':fields.float('Warehouse2'),
        'qty_warehouse3':fields.float('Warehouse3'),
        'qty_warehouse4':fields.float('Warehouse4'),
        'qty_warehouse5':fields.float('Warehouse5'),
        'discount_price':fields.float('Discount Price', digits_compute=dp.get_precision('Product Price')),
        'supplier_ref':fields.char('Supplier Ref'),
        'order_wh1':fields.float('Order for Warehouse1'),
        'order_wh2':fields.float('Order for Warehouse1'),
        'order_wh3':fields.float('Order for Warehouse1'),
        'order_wh4':fields.float('Order for Warehouse1'),
        'order_wh5':fields.float('Order for Warehouse1'),
        
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
