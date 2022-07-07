from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Customers:
    CustomerId: int
    CustomerName: str
    BilltoCustomerID: int
    CustomerCategoryID:int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: float
    AccountOpenedDate: date
    StandardDiscountPercentage: float
    IsStatementSend: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPosition: str
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: int
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: int
    LastEditedBy: int
    ValidFrom: datetime
    ValidTo: datetime

@dataclass
class Order:
    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: date
    ExpectedDeliveryDate: date
    CustomerPurchaseOrderNumber: str
    IsUndersupplyBackordered: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: datetime
    LastEditedBy: int
    LastEditedWhen: datetime

    def __gt__(self,other):
        return self.OrderID > other.OrderID

    def __ge__(self,other):
        return self.OrderID > other.OrderID

@dataclass
class Invoices:
    InvoiceID: int
    CustomerID: int
    BillToCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalespersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: date
    CustomerPurchaseOrderNumber: str
    IsCreditNote: bool
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: str
    RunPosition: str
    ReturnedDeliveryData: str
    ConfirmedDeliveryTime: datetime
    ConfirmedReceivedBy: str
    LastEditedBy: int
    LastEditedWhen: datetime

    def __gt__(self,other):
        return self.InvoiceID > other.InvoiceID

    def __ge__(self,other):
        return self.InvoiceID > other.InvoiceID