# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from unicodedata import category
from odoo import http, fields, models, _
from odoo.tools import date_utils
from odoo.http import request, Response, JsonRequest
from odoo.exceptions import ValidationError, UserError
from datetime import datetime
import json, requests
import logging
import base64
import io
import ast
import re

_logger = logging.getLogger(__name__)

class BakingWorldApi(http.Controller):        
    def alternative_json_response(self, result=None, error=None):
        if error is not None:
            response = error
        if result is not None:
            response = result
            mime = 'application/json'
            body = json.dumps(response, default=date_utils.json_default)
            
        return Response(body, status=error and error.pop('http_status', 200) or 200,
                        headers=[('Content-Type', mime), ('Content-Length', len(body))])
        
    @http.route('/api/verification', auth='user', type='json')
    def Authorization(self, request):        
        if request.httprequest.headers.get('Authorization'):
            key = request.httprequest.headers.get('Authorization').split(" ")[1]                
            if key != 'KEDATECHTEST':                                                
                body = {
                    "code": 401,
                    "success": False,
                    "message": "Unauthorized.",
                    "data": []
                }
                request._json_response = self.alternative_json_response.__get__(request, JsonRequest)
                return body
            else:
                return True
        else:
            body = {
                "code": 401,
                "success": False,
                "message": "Token not found in your header.",
                "data": []
            }
            request._json_response = self.alternative_json_response.__get__(request, JsonRequest)
            return body

    @http.route('/api/material/search', type='json', auth='public', methods=['GET'], csrf=False)
    def material_search_all(self, **kw):
        isauth = self.Authorization(request)
        if isauth == True:            
            OMaterial = request.env['material.material']            
            materials = OMaterial.sudo().search([])
            
            values = []
            for material in materials:                
                data = {
                    'product_name': material.name,
                    'default_code': material.default_code,
                    'product_uom': material.product_uom.name,
                    'product_type': material.product_type,
                    'price_unit': material.price_unit,
                    'partner_id': material.partner_id.name            
                }  
                values.append(data)              
            body = {
                "code": 200,
                "success": True,
                "message": "Success retreive " + str(len(materials)) + " Product in Pricelist",
                "data": values
            }
            # body = values
            request._json_response = self.alternative_json_response.__get__(request, JsonRequest)
            return body               
        else:return isauth