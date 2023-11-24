"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

from flask import make_response, abort




# Data to serve with our API
PEOPLE = {
    "Muhammad Hanaul Rofiq": {
        "nama": "Muhammad Hanaul Rofiq",
        "Email":"rofiqhanaul@gmail.com",

    },
}


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(Email):
    """
    This function responds to a request for /api/people/{Email}
    with one matching person from people
    :param Email:   last name of person to find
    :return:        person matching Email
    """
    # Does the person exist in people?
    if Email in PEOPLE:
        person = PEOPLE.get(Email)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {Email} not found".format(Email=Email)
        )

    return person


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    Email= person.get("Email", None)
    nama = person.get("nama", None)

    # Does the person exist already?
    if Email not in PEOPLE and Email is not None:
        PEOPLE[Email] = {
            "Email": Email,
            "nama": nama,
        }
        return make_response(
            "{Email} successfully created".format(Email=Email), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {Email} already exists".format(Email=Email),
        )


def update(Email, person):
    """
    This function updates an existing person in the people structure
    :param Email:   Email of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    if Email in PEOPLE:
        PEOPLE[Email]["nama"] = person.get("nama")

        return PEOPLE[Email]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with Email {Email} not found".format(Email=Email)
        )


def delete(Email):
    """
    This function deletes a person from the people structure
    :param Email:   Email of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if Email in PEOPLE:
        del PEOPLE[Email]
        return make_response(
            "{Email} successfully deleted".format(Email=Email), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with Email {Email} not found".format(Email=Email)
        )