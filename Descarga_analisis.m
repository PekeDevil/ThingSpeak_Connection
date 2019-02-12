[Canal1,timestampsC1] = thingSpeakRead(697555,'ReadKey','QD9KBRC6YEKXF7L8','Fields',[1,2],'NumPoints',8000);
[Canal2,timestampsC2] = thingSpeakRead(697556,'ReadKey','2UFBSOSHY29Y3FNI','Fields',[1,2],'NumPoints',8000);

[Canal1_Filas, Canal1_Columnas] = size(Canal2);
[Canal2_Filas, Canal2_Columnas] = size(Canal2);

indice = 1;
for index_filas = 1:Canal1_Filas
    for index_columnas = 1:Canal1_Columnas
    ArrayDatos(indice, index_columnas) = Canal1(index_filas, index_columnas);
    indice2 = indice+1;
    ArrayDatos(indice2, index_columnas) = Canal2(index_filas, index_columnas);
    end       
        indice = indice+2;           
end
       
    ArrayTiempo = timestampsC1;
    indice = 1;
for index_filas = 1:Canal1_Filas
    ArrayTiempo(indice) = timestampsC1(index_filas);
    indice2 = indice+1;
    ArrayTiempo(indice2) = timestampsC2(index_filas);
    indice = indice+2;           
end

figure(1);
subplot(2,1,1);
x=ArrayDatos(:,1);
plot(ArrayTiempo, x,'red', 'linewidth',3);
grid on
title({'Humedad'})
xlabel('Cada muestra equivale a 10 segundos');
ylabel("%");
subplot(2,1,2);
x=ArrayDatos(:,2);
plot(ArrayTiempo, x,'blue', 'linewidth',3);
grid on
title({'Temperatura'})
xlabel('Cada muestra equivale a 10 segundos');
ylabel("ºC");

[Filas_totales, Columnas_totales] = size(ArrayDatos);

for muestras = 1:Filas_totales
    if rem (muestras,60) == 0 
        Funcion_sensacion(ArrayDatos(muestras,1),ArrayDatos(muestras,2));
    end
end