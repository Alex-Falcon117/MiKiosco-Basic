from flet import (
    Container,
    Column,
    Row,
    TextField,
    Text,
    ElevatedButton,
    IconButton,
    OutlinedButton,
    Divider,
    DataTable,
    DataColumn,
    border,
    BorderSide,
    MainAxisAlignment,
    Icons,
    Icon,
    Colors,
    VerticalDivider,
    ScrollMode,
    ResponsiveRow,
    ExpansionPanel,
    ExpansionPanelList,
    padding,
    AlertDialog,
    AutoComplete,
    SearchBar,
    ListView,
    RoundedRectangleBorder,
)

from controllers.controller_combos import ControllerCombo as my_controller


class ViewCombos(Container):

    color_black26 = Colors.BLACK26
    hor_divider = Divider()
    ver_divider = VerticalDivider()

    ###Controles de Crear Combos
    tf_nombre_combo = TextField(label="Nombre del combo", expand=True)
    tf_descuento_combo = TextField(
        label="Descuento general",
        suffix_icon=Icons.PERCENT_ROUNDED,
        expand=True,
    )
    tf_total_combo = TextField(
        prefix_icon=Icons.ATTACH_MONEY_OUTLINED,
        label="Precio del combo",
        expand=True,
    )
    ebtn_agregar_producto = ElevatedButton(
        text="Agregar producto", icon=Icons.ADD_CIRCLE_OUTLINE
    )
    ebtn_guardar_combo = ElevatedButton(text="Guardar", icon=Icons.SAVE_OUTLINED)
    ibtn_cancelar_combo = IconButton(tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED)
    ibtn_cerrar_agregar_producto = IconButton(icon=Icons.CLOSE)

    ebtn_ver_combos = ElevatedButton(text="Ver combos", icon=Icons.DISCOUNT_OUTLINED)
    ebtn_editar_combo2 = ElevatedButton(text="Editar", icon=Icons.EDIT_OUTLINED)
    obtn_quitar_combo = OutlinedButton(text="Quitar", icon=Icons.CANCEL_OUTLINED)

    ###Controles de Combos
    ebtn_crear_combo = ElevatedButton(
        text="Crear combo", icon=Icons.ADD_CIRCLE_OUTLINE_OUTLINED
    )
    ebtn_editar_combo = ElevatedButton(text="Editar", icon=Icons.EDIT_OUTLINED)
    obtn_eliminar_combo = OutlinedButton(text="Eliminar", icon=Icons.DELETE_OUTLINE)

    ###Controles de Dialog seleccionar producto
    lv_productos = ListView()
    sb_buscar_producto = SearchBar(
        bar_hint_text="Buscar un producto",
        view_hint_text="Selecciona un color de las sugerencias",
        view_shape=RoundedRectangleBorder(radius=5),
        bar_shape=RoundedRectangleBorder(radius=5),
        controls=[lv_productos],
    )
    ac_buscar_producto = AutoComplete(
        suggestions=my_controller.resultado_burqueda_producto()
    )
    tf_cantidad_producto = TextField(label="Cantidad", width=100)
    txt_subtotal = Text(value="Subtotal: $0")
    ebtn_agregar = ElevatedButton(text="Agregar")
    ibtn_cerrar_seleccionar_productos = IconButton(
        tooltip="Cancelar", icon=Icons.CLOSE_ROUNDED
    )
    txt_mensaje_alerta = Text(color=Colors.RED)

    dt_combos = DataTable(
        show_checkbox_column=True,
        checkbox_horizontal_margin=0,
        border=border.all(1),
        border_radius=5,
        vertical_lines=BorderSide(1),
        heading_row_color=color_black26,
        sort_column_index=0,
        sort_ascending=True,
        columns=[
            DataColumn(
                numeric=True,
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="ID"),
            ),
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Producto"),
            ),
            DataColumn(
                numeric=True,
                label=Text(value="Cantidad"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
            DataColumn(
                numeric=True,
                label=Text(value="Subtotal"),
                heading_row_alignment=MainAxisAlignment.START,
            ),
        ],
    )

    dt_promociones_activas = DataTable(
        # expand=True,
        # data_row_max_height=40,
        show_checkbox_column=True,
        checkbox_horizontal_margin=0,
        border=border.all(1),
        border_radius=5,
        vertical_lines=BorderSide(1),
        heading_row_color=color_black26,
        sort_column_index=0,
        sort_ascending=True,
        columns=[
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Productos"),
            ),
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Cantidad"),
            ),
            DataColumn(
                heading_row_alignment=MainAxisAlignment.START,
                label=Text(value="Total"),
            ),
        ],
    )

    ep_venta = ExpansionPanel(
        header=Container(
            padding=padding.only(left=5),
            content=Row(
                expand=True,
                controls=[Text(value="hola")],
            ),
        ),
        expand=True,
    )
    ep_venta_1 = ExpansionPanel(expand=True, content=Text(value="Hola"))
    ep_venta_2 = ExpansionPanel(expand=True, content=Text(value="Hola"))

    eplist_combo = ExpansionPanelList(
        expand=True,
        # divider_color=color_divider,
        controls=[
            ep_venta,
            ep_venta_1,
            ep_venta_2,
        ],
    )
    cont_combos = Container(
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Column(scroll=ScrollMode.AUTO, expand=True, controls=[eplist_combo]),
                Column(
                    controls=[
                        Container(
                            expand=True,
                            bgcolor=color_black26,
                            border_radius=5,
                            padding=5,
                            content=Row(
                                alignment=MainAxisAlignment.CENTER,
                                height=40,
                                expand=True,
                                controls=[
                                    ebtn_crear_combo,
                                    ver_divider,
                                    ebtn_editar_combo,
                                    obtn_eliminar_combo,
                                ],
                            ),
                        )
                    ]
                ),
            ],
        ),
    )
    cont_crear_combos = Container(
        visible=False,
        padding=5,
        bgcolor=color_black26,
        border_radius=5,
        expand=True,
        content=Column(
            expand=True,
            controls=[
                Row(
                    controls=[
                        Icon(name=Icons.ADD_CIRCLE_OUTLINE_OUTLINED),
                        Text(value="Crear combos"),
                    ]
                ),
                hor_divider,
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(
                            expand=True,
                            controls=[
                                tf_nombre_combo,
                                tf_descuento_combo,
                                tf_total_combo,
                                ebtn_agregar_producto,
                            ],
                        ),
                        Row(
                            controls=[
                                ebtn_guardar_combo,
                                ibtn_cancelar_combo,
                            ]
                        ),
                    ],
                ),
                Column(
                    expand=True,
                    scroll=ScrollMode.AUTO,
                    controls=[ResponsiveRow(expand=True, controls=[dt_combos])],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    height=40,
                    controls=[
                        ebtn_ver_combos,
                        ver_divider,
                        ebtn_editar_combo2,
                        obtn_quitar_combo,
                    ],
                ),
            ],
        ),
    )

    ad_seleccionar_productos = AlertDialog(
        modal=True,
        content=Container(
            width=450,
            height=200,
            expand=True,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Row(
                                controls=[
                                    Icon(name=Icons.LOCAL_OFFER_OUTLINED),
                                    Text(value="Seleccione un producto"),
                                ]
                            ),
                            Row(controls=[ibtn_cerrar_seleccionar_productos]),
                        ],
                    ),
                    hor_divider,
                    Row(
                        expand=True,
                        controls=[
                            Container(height=50, width=200, content=sb_buscar_producto),
                            tf_cantidad_producto,
                            txt_subtotal,
                        ],
                    ),
                    Row(alignment=MainAxisAlignment.CENTER, controls=[ebtn_agregar]),
                    txt_mensaje_alerta,
                ],
            ),
        ),
    )

    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = Column(
            # alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[self.cont_combos, self.cont_crear_combos],
        )
