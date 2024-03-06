# -*- coding: utf-8 -*-

import os
from odoo.tests.common import TransactionCase, tagged
import logging

_logger = logging.getLogger(__name__)
info=_logger.info


class TestMaterialFlow(TransactionCase):

    def test_00_material_create(self):
        """ Testing create record for material"""
        # Test Case if The Price of Product less than 100.0
        values = {
            'name': 'Blue Jeans',
            'default_code': 'RM-0001',
            'product_uom': self.env.ref('uom.product_uom_unit').id,
            'product_type': 'jeans',
            'price_unit': 99,
            'partner_id': self.env['res.partner'].search([])[0].id            
        }
        OMaterial = self.env['material.material']  
        
        with self.assertRaises(Exception) as context:
            OMaterial.create(values)
        
        # If the return is validation then True
        self.assertTrue('Price cannot set to under 100.0' == context.exception.args[0])            
        
        # Test Case if The Price of Product greate than 100.0
        values = {
            'name': 'Blue Jeans',
            'default_code': 'RM-0001',
            'product_uom': self.env.ref('uom.product_uom_unit').id,
            'product_type': 'jeans',
            'price_unit': 100.0,
            'partner_id': self.env['res.partner'].search([])[0].id            
        }
        OMaterial = self.env['material.material']  
        OMaterial.create(values)        
        
