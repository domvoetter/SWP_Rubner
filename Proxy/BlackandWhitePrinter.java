package Proxy;

class BlackAndWhitePrinter implements Printer {
    @Override
    public void print(String document) {
        System.out.println("Printing black and white document: " + document);
    }
}
