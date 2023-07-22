import logging
from time import sleep

import flet
from flet import (
    Column,
    FloatingActionButton,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    View,
    TextField,
    ElevatedButton,
    Text,
    VerticalDivider,
    icons,
    NavigationBar,
    Image,
    AppBar,
    colors,
    Container,
    PopupMenuButton,
    margin,
    PopupMenuItem,
    padding,
)

# from views.command_table import CommandTable
# from views.item_stream_table import ItemStreamTable
# from views.incoming_fix_quotes import IncomingFixQuotes

# from ClientContext import ClientContext
# import pymongo
# import traceback
# from Commands import register_command, register_commands


# logging.basicConfig(level=logging.DEBUG)

# client_context = ClientContext()

# def update_client_id(page, new_client_id):
#     page.client_storage.set("CLIENT_ID", new_client_id)
#     client_context["CLIENT_ID"] = new_client_id
    
# def ensure_client_id(page: Page):
#     view = View()
#     text_field = TextField(
#         label="Email",
#         value="",
#     )
#     def update_and_close(e):
#         if text_field.value == "":
#             return
#         update_client_id(page, text_field.value)
#         page.views.remove(view)
#         page.update()
    
#     submit_button = ElevatedButton(
#         text="Submit",
#         on_click=lambda e: update_and_close(e),
#     )
#     view.controls.append(text_field)
#     view.controls.append(submit_button)
#     page.views.append(view)
#     page.update()
#     while client_context["CLIENT_ID"] is None:
#         sleep(0.1)
    
    
# def logout(page: Page):
#     page.client_storage.remove("CLIENT_ID")
#     page.window_destroy()
    

def main(page: Page):
    # client_context.page = page
    # if client_context.is_test:
    #     page.client_storage.remove("CLIENT_ID")
    # if page.client_storage.contains_key("CLIENT_ID") and page.client_storage.get("CLIENT_ID") is not None:
    #     client_id = page.client_storage.get("CLIENT_ID")
    #     client_context["CLIENT_ID"] = client_id
    # if client_context["CLIENT_ID"] is None:
    #     ensure_client_id(page)
    # pages = [
    #     ItemStreamTable(client_context=client_context),
    #     IncomingFixQuotes(client_context=client_context),
    #     CommandTable(client_context=client_context),
    # ]

    # def select_page():
    #     print("selected index", rail.selected_index)
    #     for index, p in enumerate(pages):
    #         p.visible = True if index == rail.selected_index else False
    #     page.update()

    # def dest_change(e):
    #     select_page()
        
    
    # def goto_page(page_index):
    #     rail.selected_index = page_index
    #     select_page()
    # client_context.commands["goto_page"] = goto_page
        
    
    connections = [
        "MongoDB Test",
        "PostgreSQL Staging",
        "MySQL Dev"
    ]    
        
    page.navigation_bar = AppBar(
            # leading= Container(
            #         content=Image(src="https://redhedge.com/wp-content/uploads/2021/07/redhedge-full-logo.png", height=70),
            #         padding=padding.only(left=10)
                    
            #     ),
            leading_width=200,
            center_title=False,
            toolbar_height=75,
            bgcolor="#282C34",
            # actions=[
            #     Container(
            #         content=PopupMenuButton(
            #             items=[
            #                 PopupMenuItem(content=Text("Client ID: " + client_context["CLIENT_ID"])),
            #                 PopupMenuItem(text="Logout", on_click=lambda e: logout(page)),
            #             ]
            #         ),
            #         margin=margin.only(left=50, right=25)
            #     )
            # ],
        )
    
    destinations = [
                NavigationRailDestination(
                    icon=icons.ADD, selected_icon=icons.ADD_OUTLINED, label="Add connection"
                )
            ]

    if connections:
        destinations.append(
            NavigationRailDestination(
                    icon=icons.VIEW_LIST, selected_icon=icons.VIEW_LIST_OUTLINED, label=connections[0]
                )
        )

        destinations.append(
            NavigationRailDestination(
                    icon=icons.VIEW_LIST, selected_icon=icons.VIEW_LIST_OUTLINED, label=connections[1]
                )
        )

        destinations.append(NavigationRailDestination(
            icon=icons.VIEW_LIST, selected_icon=icons.VIEW_LIST_OUTLINED, label=connections[2]
        )),

    rail = NavigationRail(
        selected_index=0,
        label_type="all",
        # extended=True,
        min_width=100,
        min_extended_width=400,
        # trailing=Text("Something"),
        group_alignment=-0.9,
        destinations=destinations
        # on_change=dest_change,
    )

    # select_page()

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                # Column(pages, alignment="start", expand=True),
            ],
            expand=True,
        )
    )


flet.app(target=main)