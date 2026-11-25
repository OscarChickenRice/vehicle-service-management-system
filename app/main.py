
import flet as ft

# 1. Sample inventory data
parts = [
    {"name": "Engine Oil", "quantity": 20, "minimum": 5},
    {"name": "Oil Filter", "quantity": 15, "minimum": 5},
    {"name": "Brake Pad", "quantity": 2, "minimum": 5}
]

# 2. Check stock status
def check_stock(quantity, minimum):
    if quantity < minimum:
        return "LOW STOCK"
    else:
        return "IN STOCK"

def get_low_stock_parts():
    low_stock_parts = []

    for part in parts:
        if part["quantity"] < part["minimum"]:
            low_stock_parts.append(part)

    return low_stock_parts


# 3. Update inventory data
def update_part(part_name, new_quantity):
    for part in parts:
        if part["name"] == part_name:
            part["quantity"] = new_quantity
            return True

    return False


# 4. Main application
def main(page: ft.Page):

    page.title = "Spare Parts Inventory"
    page.window.width = 500
    page.window.height = 700

    # Add input fields
    name_input = ft.TextField(
        label="Spare Part Name",
        width=400
    )

    quantity_input = ft.TextField(
        label="Quantity",
        width=400
    )

    minimum_input = ft.TextField(
        label="Minimum Stock",
        width=400
    )

    # Update input fields
    update_name_input = ft.TextField(
        label="Spare Part Name to Update",
        width=400
    )

    update_quantity_input = ft.TextField(
        label="New Quantity",
        width=400
    )

    update_message = ft.Text()

    delete_name_input = ft.TextField(
        label="Spare Part Name to Delete",
        width=400
    )
    delete_message = ft.Text()

    # Inventory display area
    parts_list = ft.Column(spacing=10)

    low_stock_list = ft.Column(spacing = 5)

    # Display inventory
    def display_parts():
        parts_list.controls.clear()

        low_stock_list.controls.clear()

        for part in parts:
            status = check_stock(
                part["quantity"],
                part["minimum"]
            )

            if status ==  "LOW STOCK":
                low_stock_list.controls.append(
                    ft.Text(
                        f"{part['name']} is running low! "
                        f"Only {part['quantity']} unis remaining.",
                        color="red"
                    )
                )

            status_color = "red" if status == "LOW STOCK" else "green"

            parts_list.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(part["name"], width=150),
                        ft.Text(str(part["quantity"]), width=60),
                        ft.Text(status, color=status_color)
                    ]
                )
            )

        page.update()

    # Add new spare part
    def add_part(e):
        name = name_input.value.strip()

        try:
            quantity = int(quantity_input.value)
            minimum = int(minimum_input.value)

            if not name or quantity < 0 or minimum < 0:
                raise ValueError

        except ValueError:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please enter valid information")
            )
            page.snack_bar.open = True
            page.update()
            return

        new_part = {
            "name": name,
            "quantity": quantity,
            "minimum": minimum
        }

        parts.append(new_part)

        name_input.value = ""
        quantity_input.value = ""
        minimum_input.value = ""

        display_parts()

        page.snack_bar = ft.SnackBar(
            content=ft.Text("Spare part added successfully")
        )
        page.snack_bar.open = True
        page.update()

    # Update spare part
    def update_part_clicked(e):
        name = update_name_input.value.strip()

        try:
            new_quantity = int(update_quantity_input.value)

            if not name or new_quantity < 0:
                raise ValueError

        except ValueError:
            update_message.value = "Please enter valid information!"
            page.update()
            return

        result = update_part(name, new_quantity)

        if result:
            update_message.value = "Spare part updated successfully!"
            update_name_input.value = ""
            update_quantity_input.value = ""
            display_parts()
        else:
            update_message.value = "Spare part not found!"
            page.update()

    def delete_part(part_name):
        for part in parts:
            if part["name"] == part_name:
                parts.remove(part)
                return True

        return False


    def delete_part_clicked(e):


        name = delete_name_input.value.strip()

        if not name:
            delete_message.value = "Please enter a valid spare part name!"
            page.update()
            return

        result = delete_part(name)

        if result:
            delete_message.value = "Spare part deleted successfully!"
            delete_name_input.value = ""
            display_parts()

        else:
            delete_message.value = "Spare part not found!"
            page.update()

    # App interface
    page.add(
        ft.Text(
            "Spare Parts Inventory",
            size=25,
            weight=ft.FontWeight.BOLD
        ),

        ft.Divider(),

        name_input,
        quantity_input,
        minimum_input,

        ft.Button(
            "Add Spare Part",
            on_click=add_part
        ),

        ft.Divider(),

        ft.Text(
            "Update Spare Part",
            size=20,
            weight=ft.FontWeight.BOLD
        ),

        update_name_input,
        update_quantity_input,

        ft.Button(
            "Update Quantity",
            on_click=update_part_clicked
        ),

        update_message,

        ft.Divider(),

        ft.Text(
            "Delete Spare Part",
            size=20,
            weight=ft.FontWeight.BOLD
        ),

        delete_name_input,

        ft.Button(
            "Delete Spare Part",
            on_click=delete_part_clicked
        ),
        delete_message,

        ft.Divider(),

        ft.Text(
            "Current Inventory",
            size=20,
            weight=ft.FontWeight.BOLD
        ),

        ft.Row(
            controls=[
                ft.Text("Part Name", width=150, weight=ft.FontWeight.BOLD),
                ft.Text("Qty", width=60, weight=ft.FontWeight.BOLD),
                ft.Text("Status", weight=ft.FontWeight.BOLD)
            ]
        ),

        ft.Text(
            "Low Stock Alerts",
            size = 20,
            weight=ft.FontWeight.BOLD,
            color="red"
        ),

        low_stock_list,

        ft.Divider(),

        parts_list
    )

    display_parts()


ft.run(main)
