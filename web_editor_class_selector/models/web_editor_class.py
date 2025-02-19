from odoo import fields, models


class WebEditorClass(models.Model):
    _name = "web.editor.class"
    _description = "Web editor class selector"
    _order = "sequence,id"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    class_name = fields.Char(
        required=True,
        help="The class name to be added to the tag. "
        "It must be created in the CSS file.",
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("class_name_uniq", "unique(class_name)", "Class name must be unique")
    ]
