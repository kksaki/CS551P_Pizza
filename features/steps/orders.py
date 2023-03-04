from behave import given, when, then

@given(u'I navigate to the orders pages')
def nav(context):
    """ 
    Navigate to the customers page
    """
    context.browser.get('https://gongvillage-apollocarrot-5000.codio-box.uk//orders')

@when(u'I click on the link to customer details')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('2').click()

@then(u'I should see the order for that customer')
def details(context):
    """ 
    if successful, then we should be directed to the customer page
    """

    print(context.browser.page_source)
    assert context.browser.current_url == 'https://gongvillage-apollocarrot-5000.codio-box.uk//order_details/2'
    assert '01595 Amanda Loaf' in context.browser.page_source