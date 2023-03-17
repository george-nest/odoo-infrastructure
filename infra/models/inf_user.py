from odoo import fields, models, api, exceptions, _
import datetime
#
# class InfUser(models.Model):
#     _name = 'infra.inf_user'
#     _description = 'User (infrastructure)'
#     _inherit = 'res.partner'
#
#     ukrname = fields.Char(
#         required=True,)
#     # active = fields.Boolean(
#     #     default=True, )
#

class InfUser(models.Model):
    _name = 'infra.inf_user'

    channel_ids = fields.Many2many('my.channel', 'infra_inf_user_channel_rel', 'user_id', 'channel_id')

class Partner(models.Model):
    _inherit = 'res.partner'

    channel_ids = fields.Many2many('my.channel', 'res_partner_channel_rel', 'partner_id', 'channel_id')

    translate_name = fields.Char(
        required=True,
        compute='_compute_translate_name')
        # recurcive=True, store=True, )

    preferred_language = fields.Selection(
        [('en_US', 'English'),
         ('fr_FR', 'French'),
         ('es_ES', 'Spanish')],
        string='Preferred Language',
        default='en_US',
    )

    @api.depends()
    def _compute_translate_name(self):
        # self.translate_name = "depends"
        for rec in self:
            if rec.name:
                rec.translate_name = '%s / %s' \
                                    % ("rec.ctranslate_name", rec.name)
            else:
                rec.translate_name = '%s / %s' \
                                     % ("rec.ctranslate_name", rec.name)
                # rec.translate_name = rec.name
