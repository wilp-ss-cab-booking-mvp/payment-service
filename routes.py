# Handles payment endpoints with JWT and booking validation
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Payment
import requests

bp = Blueprint("payment_bp", __name__)

BOOKING_SERVICE_URL = "http://booking:5000"

#/pay – Make a Payment
@bp.route("/pay", methods=["POST"])
@jwt_required()
def make_payment():
    data = request.get_json()

    # Validate booking with booking service
    booking_id = data.get("booking_id")
    try:
        booking_resp = requests.get(f"{BOOKING_SERVICE_URL}/bookings/{booking_id}")
        if booking_resp.status_code != 200:
            return jsonify({"error": "Invalid booking ID"}), 404
    except requests.RequestException as e:
        return jsonify({"error": "Booking service not reachable"}), 500
    
    payment = Payment(
        booking_id=data["booking_id"],
        amount=data["amount"],
        status=data.get("status", "paid")
    )
    db.session.add(payment)
    db.session.commit()
    return jsonify({"message": "Payment successful", "payment_id": payment.id}), 201


#/payments – Get All Payments
@bp.route("/payments", methods=["GET"])
def list_payments():
    payments = Payment.query.all()
    return jsonify([p.to_dict() for p in payments])