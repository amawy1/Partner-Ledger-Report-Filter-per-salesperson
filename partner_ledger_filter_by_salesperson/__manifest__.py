# -*- coding: utf-8 -*-
{
    'name': "partner_ledger_filter_by_salesperson",
    'author': "Odoo Developer",
    'version': '15.0',
    'depends': ['base', 'account_accountant', 'account_reports'],
    'data': [
        'views/partner_ledger_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'partner_ledger_filter_by_salesperson/static/src/js/partner_ledger_filter.js',
        ],
    },
    'price': 30.00,
    'currency': 'USD',
}
