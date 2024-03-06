# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _, tools
from odoo.exceptions import UserError, ValidationError

class MaterialMaterial(models.Model):
    _name = "material.material"

    @api.depends('company_id')
    def _compute_currency_id(self):
        main_company = self.env['res.company']._get_main_company()
        for template in self:
            template.currency_id = template.company_id.sudo().currency_id.id or main_company.currency_id.id
    
    @tools.ormcache()
    def _get_default_uom_id(self):
        # Deletion forbidden (at least through unlink)
        return self.env.ref('uom.product_uom_unit')
    
    @api.depends_context('display_default_code')
    def _compute_display_name(self):
        # `display_name` is calling `name_get()`` which is overidden on product
        # to depend on `display_default_code` and `seller_id`
        return super()._compute_display_name()
    
    @api.constrains('price_unit')
    def _check_price(self):
        if self.price_unit < 100:
            raise ValidationError(_('Price cannot set to under 100.0'))
        return True

    name = fields.Char('Name', required=True, index=True, copy=False, default='New')
    default_code = fields.Char('Internal Reference', index=True)    
    taxes_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', default=_get_default_uom_id)    
    product_type = fields.Selection([('fabric','Fabric'),
                                      ('jeans','Jeans'),
                                      ('cotton','Cotton')], required=True, string='Type')
    price_unit = fields.Monetary(string='Unit Price', required=True, digits='Product Price')
    currency_id = fields.Many2one(
        'res.currency', 'Currency', compute='_compute_currency_id')
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True, change_default=True, tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
    
    company_id = fields.Many2one(
        'res.company', 'Company', index=1)

