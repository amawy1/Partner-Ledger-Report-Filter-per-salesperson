# -*- coding: utf-8 -*-
{
    'name': "partner_ledger_filter_by_salesperson",
    'author': "Ahmed Ali",
    'version': '15.1',
    'depends': ['base', 'account_accountant', 'account_reports'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner_ledger_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'partner_ledger_filter_by_salesperson/static/src/js/partner_ledger_filter.js',
        ],
    },
}
