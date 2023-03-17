# -*- coding: utf-8 -*-
# from odoo import http


# class Infra(http.Controller):
#     @http.route('/infra/infra', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infra/infra/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('infra.listing', {
#             'root': '/infra/infra',
#             'objects': http.request.env['infra.infra'].search([]),
#         })

#     @http.route('/infra/infra/objects/<model("infra.infra"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infra.object', {
#             'object': obj
#         })
