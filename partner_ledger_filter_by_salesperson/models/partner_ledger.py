from odoo import models, api, _
import logging

_logger = logging.getLogger(__name__)

class ReportPartnerLedgerCustom(models.AbstractModel):
    _inherit = 'account.partner.ledger'

    def _get_columns_name(self, options):
        columns = [
            {},
            {'name': _('Sales Person')},
            {'name': _('JRNL')},
            {'name': _('Account')},
            {'name': _('Ref')},
            {'name': _('Due Date'), 'class': 'date'},
            {'name': _('Matching Number')},
            {'name': _('Initial Balance'), 'class': 'number'},
            {'name': _('Debit'), 'class': 'number'},
            {'name': _('Credit'), 'class': 'number'}
        ]

        if self.user_has_groups('base.group_multi_currency'):
            columns.append({'name': _('Amount Currency'), 'class': 'number'})

        columns.append({'name': _('Balance'), 'class': 'number'})
        return columns



    def _get_options(self, previous_options=None):
        if not isinstance(previous_options, dict):
            previous_options = {}

        options = super(ReportPartnerLedgerCustom, self)._get_options(previous_options)
        options['salesperson_id'] = previous_options.get('salesperson_id', []) or []
        return options

    def _get_lines(self, options, line_id=None):
        lines = super(ReportPartnerLedgerCustom, self)._get_lines(options, line_id)

        filtered_lines = []
        selected_salesperson_ids = list(map(int, options.get('salesperson_id', [])))

        if not selected_salesperson_ids:
            return lines

        for line in lines:
            partner_id = line.get('partner_id')
            if partner_id:
                partner = self.env['res.partner'].browse(int(partner_id))
                if partner.exists() and partner.user_id.id in selected_salesperson_ids:
                    filtered_lines.append(line)
                elif 'move_line_ids' in line:
                    move_lines = self.env['account.move.line'].browse(line['move_line_ids'])
                    move_lines_filtered = move_lines.filtered(lambda l: l.create_uid.id in selected_salesperson_ids)
                    if move_lines_filtered:
                        line['move_line_ids'] = move_lines_filtered.ids
                        line['unfoldable'] = True
                        filtered_lines.append(line)
                    else:
                        _logger.info(f"Move lines for partner '{partner.name}' (ID {partner.id}) did not match any selected salesperson.")
            else:
                filtered_lines.append(line)

        return filtered_lines

    @api.model
    def _get_report_line_partner(self, options, partner, initial_balance, debit, credit, balance):
        line = super(ReportPartnerLedgerCustom, self)._get_report_line_partner(
            options, partner, initial_balance, debit, credit, balance
        )

        if partner and partner.user_id:
            salesperson_name = partner.user_id.name
        else:
            salesperson_name = _('No Salesperson')

        line['columns'].insert(0, {'name': salesperson_name})
        return line

    @api.model
    def _get_report_line_move_line(self, options, partner, aml, cumulated_init_balance, cumulated_balance):
        line = super(ReportPartnerLedgerCustom, self)._get_report_line_move_line(
            options, partner, aml, cumulated_init_balance, cumulated_balance
        )

        if partner and partner.user_id:
            salesperson_name = partner.user_id.name
        else:
            salesperson_name = _('No Salesperson')

        line['columns'].insert(0, {'name': salesperson_name})
        return line
