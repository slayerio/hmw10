def perform_action(action):
    action_dict = {
        'add': 'Adding item',
        'delete': 'Deleting item',
        'update': 'Updating item'
        }
    print(action_dict.get(action, 'Unknown action'))

perform_action('reverse')
perform_action('add')
# intentionally didn't use return because its once







# def perform_action(action):
#     match action:
#         case 'add':
#             return 'Adding item'
#         case 'delete':
#             return 'Deleting item'
#         case 'update':
#             return 'Updating item'
#         case _:
#             return 'Unknown action'
#
#
# result = perform_action('add')
# print(result)