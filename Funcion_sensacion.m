function Sensacion(Temperatura,Humedad)

Temp_Ajuste = 0;
Humedad_Ajuste = 0;
%Funciones de pertenencia

%%Temperatura
if (Temperatura < 0)
    u_frio = 1;
    u_fresco = 0;
    u_templado = 0;
    u_calor = 0;
else if (Temperatura >= 0) && (Temperatura < 10)
        u_frio = -0.1*Temperatura + 1;
        u_fresco = 0.1*Temperatura;
    else if (Temperatura >= 10) && (Temperatura < 20)
            Temp_ajuste = Temperatura - 10;
            u_fresco = -0.1*Temp_ajuste + 1;
            u_templado = 0.1*Temp_ajuste;
            u_calor = 0;
            u_frio = 0;
        else if (Temperatura >= 20) && (Temperatura < 30)
                Temp_ajuste = Temperatura - 20;
                u_templado = -0.1*Temp_ajuste + 1;
                u_calor = 0.1*Temp_ajuste;
                u_frio = 0;
                u_fresco = 0;
            else if (Temperatura >= 30)
                    u_templado = 0;
                    u_calor = 1;
                    u_frio = 0;
                    u_fresco = 0;
                end
            end
        end
    end
end

%%Humedad
if (Humedad >= 0) && (Humedad < 10)
    h_baja = 1;
    h_media = 0;
    h_alta = 0;
else if (Humedad >= 10) && (Humedad < 50)
        Humedad_Ajuste = Humedad - 10;
        h_baja = -0.02*Humedad_Ajuste + 1;
        h_media = 0.02*Humedad_Ajuste;
        h_alta = 0;
    else if (Humedad >= 50) && (Humedad < 90)
            Humedad_Ajuste = Humedad - 50;
            h_media = -0.02*Humedad_Ajuste + 1;
            h_alta = 0.02*Humedad_Ajuste;
            h_baja = 0;
        else if (Humedad >= 90)
                h_media = 0;
                h_alta = 1;
                h_baja = 0;
            end 
        end
    end
end

%%Estados
Soportable1 = min(u_frio,h_baja) * 100;
Malo1 = min(u_frio,h_media) * 100;
Inclemente1 = min(u_frio,h_alta) * 100;
Agradable1 = min(u_fresco,h_baja) * 100;
Soportable2 = min(u_fresco,h_media) * 100;
Malo2 = min(u_fresco,h_alta) * 100;
Desapercibido1 = min(u_templado,h_baja) * 100;
Agradable2 = min(u_templado,h_media) * 100;
Soportable3 = min(u_templado,h_alta) * 100;
Desapercibido2 = min(u_calor,h_baja) * 100;
Desapercibido3 = min(u_calor,h_media) * 100;
Agradable3 = min(u_calor,h_alta) * 100;

Soportable = Soportable1 + Soportable2 + Soportable3;
Malo = Malo1 + Malo2;
Inclemente = Inclemente1;
Desapercibido = Desapercibido1 + Desapercibido2 + Desapercibido3;
Agradable = Agradable1 + Agradable2 + Agradable3;

S = 'La sensacion es soportable';
M = 'La sensacion es mala';
D = 'La sensacion es desapercibidda';
K = 'La sensacion es soportable';
I = 'La sensacion es inclemente';

if (Soportable > Malo) && (Soportable > Inclemente) && (Soportable > Desapercibido) && (Soportable > Agradable)
    disp(S);
else if (Soportable < Malo) && (Malo > Inclemente) && (Malo > Desapercibido) && (Malo > Agradable)
        disp(M);
        else if (Soportable < Inclemente) && (Inclemente > Malo) && (Inclemente > Desapercibido) && (Inclemente > Agradable)
                disp(I);
                else if (Soportable < Desapercibido) && (Desapercibido > Malo) && (Inclemente < Desapercibido) && (Desapercibido > Agradable)
                disp(D);
                else if (Soportable < Agradable) && (Agradable > Malo) && (Inclemente < Agradable) && (Agradable > Desapercibido)
                disp(K);
                    end
                    end
            end
    end
end
end

