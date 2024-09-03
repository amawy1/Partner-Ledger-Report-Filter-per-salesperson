# -*- coding: utf-8 -*-
{
    'name': "partner_ledger_filter_by_salesperson",
    'description': """
        <h1>Partner Ledger Filter by Salesperson</h1>
            <p>This module adds a filter by salesperson to the partner ledger report.</p>
                <ul>
                    <li>Show salesperson column in partner ledger report.</li>
                    <li>Ability to filter by salesperson</li>
                    <li>Ability to export report with salesperson</li>
                    <li>Compatible with Odoo 15.0.</li>
                    <li>Easy to use and integrates seamlessly with existing reports.</li>
                </ul>
        """,
    'category': 'Accounting',
    'author': "Odoo Developer",
    'version': '15.0',
    'depends': ['base', 'account_accountant', 'account_reports'],
    'license': 'LGPL-3',
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
